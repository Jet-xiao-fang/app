#!/usr/bin/env python3
"""
MySQL 智能代理 - 使用 DeepSeek + LangGraph Memory
支持自然语言查询 MySQL 数据库，非数据库问题使用普通 LLM 对话。
"""

import os
import sys
import json
import re
from typing import TypedDict, Annotated, Literal

from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver


# 加载环境变量
load_dotenv()

# ===================== 配置区 =====================
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://baitong-ai.gree.com/openapi/cllm")
MODEL_NAME = "deepseek-chat"
TEMPERATURE = 0.0

MYSQL_URI = os.getenv("MYSQL_URI")

INCLUDE_TABLES = None
SAMPLE_ROWS = 2

VERBOSE = True
HANDLE_PARSING_ERRORS = True
MAX_ITERATIONS = 5

# 普通 LLM 对话的系统提示
GENERAL_SYSTEM_PROMPT = "你是一个乐于助人的AI助手，可以回答任何问题。"
# =================================================


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    intent: str          # "sql" 或 "general"
    reasoning: str       # 分类理由


def build_sql_agent():
    """初始化数据库、模型和 SQL Agent"""
    if not DEEPSEEK_API_KEY:
        raise ValueError("请在 .env 文件中设置 DEEPSEEK_API_KEY")
    if not MYSQL_URI:
        raise ValueError("请在 .env 文件中设置 MYSQL_URI")

    print("正在连接数据库...")
    db = SQLDatabase.from_uri(
        MYSQL_URI,
        include_tables=INCLUDE_TABLES,
        sample_rows_in_table_info=SAMPLE_ROWS
    )
    print(f"已连接，可访问的表：{db.get_usable_table_names()}")

    print(f"正在初始化 DeepSeek 模型（{MODEL_NAME}）...")
    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        openai_api_key=DEEPSEEK_API_KEY,
        openai_api_base=DEEPSEEK_BASE_URL
    )

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=VERBOSE,
        handle_parsing_errors=HANDLE_PARSING_ERRORS,
        max_iterations=MAX_ITERATIONS,
    )
    return agent, llm


def classify_intent(llm, question: str) -> tuple[bool, str]:
    """
    使用普通 LLM 调用 + JSON 解析判断意图。
    返回 (is_sql_related, reasoning)
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个严格的意图分类器。请输出一个 JSON 对象，包含两个字段：is_sql_related (布尔值) 和 reasoning (字符串)。不要输出其他任何内容。"),
        ("human", "问题：{question}\n该问题是否需要查询数据库（例如统计、筛选、计算、查看记录、分析数据）？")
    ])
    chain = prompt | llm
    response = chain.invoke({"question": question})
    content = response.content.strip()
    
    try:
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            data = json.loads(json_str)
            is_sql = data.get("is_sql_related", False)
            reasoning = data.get("reasoning", "")
            return is_sql, reasoning
        else:
            raise ValueError("No JSON found")
    except Exception as e:
        print(f"JSON 解析失败：{e}，原始内容：{content[:100]}，使用关键词降级")
        sql_keywords = ["表", "查询", "统计", "筛选", "计算", "记录", "分析", "数据", "select", "sql", "category", "table"]
        lower_q = question.lower()
        is_sql = any(kw in lower_q for kw in sql_keywords)
        reasoning = f"关键词匹配（问题包含{'' if is_sql else '不'}含SQL相关词）"
        return is_sql, reasoning


def build_graph(sql_agent, llm):
    """使用 LangGraph 构建带意图分类和记忆的对话流程"""

    # ----- 意图分类节点 -----
    def classify_node(state: AgentState) -> AgentState:
        messages = state["messages"]
        last_human = None
        for msg in reversed(messages):
            if isinstance(msg, HumanMessage):
                last_human = msg
                break

        if last_human is None:
            return {"messages": [AIMessage(content="请提出问题。")], "intent": "general", "reasoning": "无用户问题"}

        is_sql, reasoning = classify_intent(llm, last_human.content)
        if is_sql:
            return {"intent": "sql", "reasoning": reasoning}
        else:
            return {"intent": "general", "reasoning": reasoning}

    # ----- 普通 LLM 对话节点（非 SQL 问题）-----
    def general_node(state: AgentState) -> AgentState:
        """使用普通 LLM 回答任何非数据库问题，保留对话历史"""
        messages = state["messages"]
        # 构造完整的对话上下文（不包含分类节点的内部消息）
        # 注意：messages 中已经包含了所有用户和 AI 的消息
        prompt = ChatPromptTemplate.from_messages([
            ("system", GENERAL_SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="history")
        ])
        chain = prompt | llm
        response = chain.invoke({"history": messages})
        return {"messages": [AIMessage(content=response.content)]}

    # ----- SQL Agent 节点 -----
    def sql_node(state: AgentState) -> AgentState:
        messages = state["messages"]
        human_messages = [m for m in messages if isinstance(m, HumanMessage)]
        if not human_messages:
            return {"messages": [AIMessage(content="请先输入问题。")]}

        last_human = human_messages[-1]

        # 构造历史对话（不包括当前问题）
        history_text = []
        for msg in messages:
            if msg is last_human:
                continue
            if isinstance(msg, HumanMessage):
                history_text.append(f"用户: {msg.content}")
            elif isinstance(msg, AIMessage):
                # 排除可能的路由辅助消息
                if not msg.content.startswith("__ROUTE__"):
                    history_text.append(f"助手: {msg.content}")

        history_block = "\n".join(history_text).strip()

        if history_block:
            agent_input = f"""以下是之前的对话历史：
{history_block}

当前用户问题：
{last_human.content}
请结合上下文理解用户意图。如果用户本轮问题依赖上一轮条件（例如“只看广东”“按天统计”“换成最近7天”），请自动继承并补全查询条件后再查询数据库。
"""
        else:
            agent_input = last_human.content

        result = sql_agent.invoke({"input": agent_input})
        answer = result["output"]
        return {"messages": [AIMessage(content=answer)]}

    # ----- 路由函数 -----
    def route_after_classify(state: AgentState) -> Literal["sql_node", "general_node"]:
        if state.get("intent") == "sql":
            return "sql_node"
        else:
            return "general_node"

    # ----- 构建图 -----
    builder = StateGraph(AgentState)
    builder.add_node("classify", classify_node)
    builder.add_node("general_node", general_node)
    builder.add_node("sql_node", sql_node)

    builder.add_edge(START, "classify")
    builder.add_conditional_edges("classify", route_after_classify)
    builder.add_edge("sql_node", END)
    builder.add_edge("general_node", END)

    memory = InMemorySaver()
    app = builder.compile(checkpointer=memory)
    return app


def main():
    sql_agent, llm = build_sql_agent()
    app = build_graph(sql_agent, llm)

    print("Agent 已就绪，输入 'exit' 退出程序")
    print("提示：数据库问题 → SQL Agent；其他问题 → 普通 AI 对话\n")

    thread_id = "cli-session-001"

    while True:
        try:
            question = input("请输入您的问题: ").strip()
            if question.lower() in ("exit", "quit", "q"):
                print("再见！")
                break
            if not question:
                continue

            config = {"configurable": {"thread_id": thread_id}}

            result = app.invoke(
                {"messages": [HumanMessage(content=question)], "intent": "", "reasoning": ""},
                config=config
            )

            last_message = result["messages"][-1]
            print(f"回答：{last_message.content}\n")

        except (EOFError, KeyboardInterrupt):
            print("\n用户中断，再见！")
            break
        except Exception as e:
            print(f"发生错误：{e}\n")


if __name__ == "__main__":
    main()
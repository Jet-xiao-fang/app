#!/usr/bin/env python3
"""
MySQL 智能代理 - 使用 DeepSeek + LangGraph Memory
基于 LangChain create_sql_agent，支持自然语言查询 MySQL 数据库，
并通过 LangGraph 1.2.4 实现多轮会话记忆。
"""

import os
import sys
from typing import TypedDict, Annotated

from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
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
# =================================================
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


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
    return agent
def build_graph(sql_agent):
    """使用 LangGraph 构建带记忆的对话流程"""

    def chat_node(state: AgentState) -> AgentState:
        messages = state["messages"]

        # 找到最后一条用户消息
        last_human_message = None
        for msg in reversed(messages):
            if isinstance(msg, HumanMessage):
                last_human_message = msg
                break

        if last_human_message is None:
            return {"messages": [AIMessage(content="请先输入问题。")]}

        # 简单做法：把历史对话拼接进当前输入，让 SQL Agent 感知上下文
        history_text = []
        for msg in messages[:-1]:  # 最后一条是当前问题，不重复加
            role = "用户" if isinstance(msg, HumanMessage) else "助手"
            history_text.append(f"{role}: {msg.content}")

        history_block = "\n".join(history_text).strip()

        if history_block:
            agent_input = f"""以下是之前的对话历史：
{history_block}

当前用户问题：
{last_human_message.content}
请结合上下文理解用户意图。如果用户本轮问题依赖上一轮条件（例如“只看广东”“按天统计”“换成最近7天”），请自动继承并补全查询条件后再查询数据库。
"""
        else:
            agent_input = last_human_message.content

        result = sql_agent.invoke({"input": agent_input})
        answer = result["output"]

        return {"messages": [AIMessage(content=answer)]}

    graph = StateGraph(AgentState)
    graph.add_node("chat_node", chat_node)
    graph.add_edge(START, "chat_node")
    graph.add_edge("chat_node", END)

    # LangGraph 短期记忆
    memory = InMemorySaver()

    app = graph.compile(checkpointer=memory)
    return app


def main():
    sql_agent = build_sql_agent()
    app = build_graph(sql_agent)

    print("Agent 已就绪，输入 'exit' 退出程序")
    print("提示：现在已支持多轮记忆，同一 thread_id 下会记住上下文。\n")

    # 你也可以改成让用户输入会话 ID
    thread_id = "cli-session-001"

    while True:
        try:
            question = input("请输入您的问题: ").strip()
            if question.lower() in ("exit", "quit", "q"):
                print("再见！")
                break
            if not question:
                continue

            config = {
                "configurable": {
                    "thread_id": thread_id
                }
            }

            result = app.invoke(
                {"messages": [HumanMessage(content=question)]},
                config=config
            )

            # 取最后一条 AI 消息
            last_message = result["messages"][-1]
            print(f"回答：{last_message.content}\n")

        except (EOFError, KeyboardInterrupt):
            print("\n用户中断，再见！")
            break
        except Exception as e:
            print(f"发生错误：{e}\n")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
MySQL 智能代理 - 使用 DeepSeek 大模型
基于 LangChain 的 create_sql_agent，支持自然语言查询 MySQL 数据库。
"""

import os
import sys
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI  # DeepSeek 兼容 OpenAI API

# 加载环境变量
load_dotenv()

# ===================== 配置区 =====================
# DeepSeek 配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://baitong-ai.gree.com/openapi/cllm")
MODEL_NAME = "deepseek-chat"        # 或 "deepseek-reasoner"（推理模型）
TEMPERATURE = 0.0                    # 0 表示确定性输出

# MySQL 配置
MYSQL_URI = os.getenv("MYSQL_URI")

# 可选：限制 Agent 只能访问哪些表（安全 + 性能）
INCLUDE_TABLES = None                # 例如 ["users", "orders"]，None 表示允许所有表
SAMPLE_ROWS = 2                      # 每个表提供多少示例数据给 LLM（帮助理解结构）

# Agent 行为参数
VERBOSE = True                       # 是否打印详细思考过程（调试用）
HANDLE_PARSING_ERRORS = True         # 自动处理解析错误
MAX_ITERATIONS = 5                   # 最大迭代次数，防止死循环
# =================================================
def main():
    # 检查必要的环境变量
    if not DEEPSEEK_API_KEY:
        raise ValueError("请在 .env 文件中设置 DEEPSEEK_API_KEY")
    if not MYSQL_URI:
        raise ValueError("请在 .env 文件中设置 MYSQL_URI")

    # 1. 连接数据库（建议使用只读用户）
    print("正在连接数据库...")
    db = SQLDatabase.from_uri(
        MYSQL_URI,
        include_tables=INCLUDE_TABLES,
        sample_rows_in_table_info=SAMPLE_ROWS
    )
    print(f"已连接，可访问的表：{db.get_usable_table_names()}")

    # 2. 初始化 DeepSeek 大模型（通过 OpenAI 兼容接口）
    print(f"正在初始化 DeepSeek 模型（{MODEL_NAME}）...")
    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        openai_api_key=DEEPSEEK_API_KEY,
        openai_api_base=DEEPSEEK_BASE_URL   # 关键：指向 DeepSeek 的 API 地址
    )

    # 3. 创建 SQL Agent
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=VERBOSE,
        handle_parsing_errors=HANDLE_PARSING_ERRORS,
        max_iterations=MAX_ITERATIONS,
        # 可选：自定义提示词（如加入数据库业务规则）
        # agent_executor_kwargs={"early_stopping_method": "generate"}
    )

    print("Agent 已就绪，输入 'exit' 退出程序\n")

    # 4. 交互循环
    while True:
        try:
            question = input("请输入您的问题: ").strip()
            if question.lower() in ("exit", "quit", "q"):
                print("再见！")
                break
            if not question:
                continue

            # 调用 Agent
            response = agent.invoke({"input": question})
            # 输出最终答案（response["output"] 是自然语言结果）
            print(f"回答：{response['output']}\n")

        except (EOFError, KeyboardInterrupt):
            print("\n用户中断，再见！")
            break
        except Exception as e:
            print(f"发生错误：{e}\n")

if __name__ == "__main__":
    main()
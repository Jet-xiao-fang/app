#!/usr/bin/env python3
"""
Impala 智能代理 - 使用 DeepSeek 大模型
基于 LangChain 和 Impyla，支持自然语言查询 Impala 数据库。
"""
import os
import sys
from dotenv import load_dotenv
from impala.dbapi import connect
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

# ===================== 配置区 =====================
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
MODEL_NAME = "deepseek-chat"
TEMPERATURE = 0.0

IMPALA_HOST = os.getenv("IMPALA_HOST", "your_impala_host")
IMPALA_PORT = int(os.getenv("IMPALA_PORT", 21050))
IMPALA_USER = os.getenv("IMPALA_USER")
IMPALA_PASSWORD = os.getenv("IMPALA_PASSWORD")
IMPALA_DATABASE = os.getenv("IMPALA_DATABASE", "default")
IMPALA_AUTH = os.getenv("IMPALA_AUTH", "PLAIN")  # 或 "GSSAPI" for Kerberos

INCLUDE_TABLES = None
SAMPLE_ROWS = 2
VERBOSE = True
HANDLE_PARSING_ERRORS = True
MAX_ITERATIONS = 5
# =================================================

def create_impala_connection():
    """创建 Impala 连接"""
    return connect(
        host=IMPALA_HOST,
        port=IMPALA_PORT,
        user=IMPALA_USER,
        password=IMPALA_PASSWORD,
        database=IMPALA_DATABASE,
        auth_mechanism=IMPALA_AUTH
    )

def main():
    if not DEEPSEEK_API_KEY:
        raise ValueError("请在 .env 文件中设置 DEEPSEEK_API_KEY")
    if not IMPALA_HOST:
        raise ValueError("请在 .env 文件中设置 IMPALA_HOST")

    # 1. 连接 Impala
    print("正在连接 Impala 数据库...")
    impala_conn = create_impala_connection()
    db = SQLDatabase.from_impala(
        connection=impala_conn,
        include_tables=INCLUDE_TABLES,
        sample_rows_in_table_info=SAMPLE_ROWS
    )
    print(f"已连接，可访问的表：{db.get_usable_table_names()}")

    # 2. 初始化 DeepSeek 模型
    print(f"正在初始化 DeepSeek 模型（{MODEL_NAME}）...")
    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        openai_api_key=DEEPSEEK_API_KEY,
        openai_api_base=DEEPSEEK_BASE_URL
    )

    # 3. 构造自定义提示词（指定 Impala 方言）
    system_prompt = (
        "你是一个 Impala SQL 专家。请根据用户的自然语言问题，生成并执行正确的 Impala SQL 查询。\n"
        "注意事项：\n"
        "1. 使用双引号包裹表名和列名（例如 SELECT \"col1\" FROM \"table\"）。\n"
        "2. 除法运算默认返回 DOUBLE 类型，可使用 CAST 控制精度。\n"
        "3. 不支持 MySQL 的 `LIMIT` 在子查询中的某些用法，请使用标准语法。\n"
        "4. 表信息会通过工具提供，请优先使用 `sql_db_schema` 查看表结构。\n"
        "5. 只返回最终答案，不要解释中间步骤。"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    # 4. 创建 SQL Agent
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        prompt=prompt,                      # 使用自定义提示词
        verbose=VERBOSE,
        handle_parsing_errors=HANDLE_PARSING_ERRORS,
        max_iterations=MAX_ITERATIONS,
    )

    print("Agent 已就绪，输入 'exit' 退出程序\n")

    # 5. 交互循环
    while True:
        try:
            question = input("请输入您的问题: ").strip()
            if question.lower() in ("exit", "quit", "q"):
                print("再见！")
                break
            if not question:
                continue
            response = agent.invoke({"input": question})
            print(f"回答：{response['output']}\n")
        except (EOFError, KeyboardInterrupt):
            print("\n用户中断，再见！")
            break
        except Exception as e:
            print(f"发生错误：{e}\n")

if __name__ == "__main__":
    main()
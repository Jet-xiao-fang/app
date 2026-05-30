import json
from openai import OpenAI

# 初始化DeepSeek客户端
client = OpenAI(
    api_key="sk-d565eee0a5764b0cb138e2b294a77b58", 
    base_url="https://api.deepseek.com"
)

# ========== 定义工具（Skills）==========
def calculator(expression: str) -> str:
    """计算器工具：计算数学表达式"""
    try:
        # 安全的eval，只允许基本数学运算
        allowed_names = {"abs": abs, "round": round}
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"计算错误: {e}"

# 工具列表（Agent的手脚）
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "执行数学计算，传入表达式如 '2+3*4' 或 '(10-5)/2'",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "要计算的数学表达式，例如 '3*7+2'"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

# ========== Agent核心逻辑 ==========
def run_agent(user_input: str, max_turns: int = 3):
    """
    简单的ReAct风格Agent
    流程：思考 -> 决定是否调用工具 -> 执行 -> 继续思考 -> 最终回答
    """
    messages = [
        {"role": "system", "content": "你是一个智能助手，可以调用工具来帮助用户。如果需要计算，调用calculator工具。"},
        {"role": "user", "content": user_input}
    ]
    
    turn = 0
    while turn < max_turns:
        turn += 1
        print(f"\n[第{turn}轮思考]")
        
        # 调用DeepSeek
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        assistant_msg = response.choices[0].message
        
        # 情况1：没有工具调用 -> 直接输出答案
        if not assistant_msg.tool_calls:
            print(f"\n[最终回答]\n{assistant_msg.content}")
            return assistant_msg.content
        
        # 情况2：有工具调用 -> 执行工具
        messages.append(assistant_msg)  # 把AI的"我想用工具"这个消息加入对话
        
        for tool_call in assistant_msg.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            print(f"[调用工具] {tool_name}({arguments})")
            
            # 执行对应的工具
            if tool_name == "calculator":
                result = calculator(arguments["expression"])
            else:
                result = f"未知工具: {tool_name}"
            
            # 把工具执行结果加入对话
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })
            print(f"[工具返回] {result}")
    
    print("[达到最大轮次]")
    return "任务执行超时"

# ========== 测试 ==========
if __name__ == "__main__":
    # 测试1：不需要工具的问题
    print("=" * 50)
    print("测试1: 普通问题")
    run_agent("今天天气怎么样？")
    
    # 测试2：需要计算的问题
    print("\n" + "=" * 50)
    print("测试2: 需要计算")
    run_agent("帮我算一下 (3 + 5) * 7 / 2 等于多少？")
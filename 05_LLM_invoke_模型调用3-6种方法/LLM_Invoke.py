# 1.导入依赖
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage,SystemMessage
from langchain_core.messages import AIMessage

#通过 python-dotenv 库读取 env 文件中的环境变量，并加载到当前运行的环境中
#load_dotenv()

# List<Messages>

# 2.实例化模型
model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("aliQwen-api"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 构建消息列表
messages = [
    SystemMessage(content="你叫小问，是一个乐于助人的AI人工助手"),
    HumanMessage(content="你是谁"),
    # AIMessage(content="我是一个AI人工助手，我的名字叫小问")
]

# 3.调用模型
response = model.invoke(messages)
print(f"响应类型：{type(response)}")
# 打印结果
print(response.content)
print(response.content_blocks)
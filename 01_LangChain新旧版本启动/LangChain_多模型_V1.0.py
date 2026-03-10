import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()



#实例化模型1
model1 = init_chat_model(
    model='qwen-plus',  #模型名称
    model_provider='openai',  #模型提供者
    api_key=os.getenv('QWEN_API_KEY'),
    base_url=os.getenv('QWEN_BASE_URL'),
)
print(model1.invoke("你是谁？").content)

print("*" * 70)


#实例化模型2
model2 = init_chat_model(
    model='deepseek-r1',
    model_provider='openai',
    api_key=os.getenv('QWEN_API_KEY'),
    base_url=os.getenv('QWEN_BASE_URL'),
)

print(model2.invoke("你是谁？ds还是千问?").content)

print("*" * 70)

# 实例化模型3 openai支持
"""
说明：
model="deepseek-chat" 和 base_url="https://api.deepseek.com" 
刚好匹配默认的 model_provider（如 deepseek），因此无需显式传入，函数内部做了智能推导
如果切换成其他模型（如 OpenAI），若默认值不匹配，就需要显式指定 model_provider="openai"。
"""
model = init_chat_model(
    model="deepseek-chat", # deepseek-chat 对应 DeepSeek-V3.2 的非思考模式
    model_provider="deepseek",
    api_key=os.getenv("DS_API_KEY"),
    base_url="https://api.deepseek.com"
)

print(model.__dict__)
print(model.invoke("你是谁").content)

# 1.导入依赖
import os
from http.client import responses

from dashscope import api_key
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import asyncio
from langchain.messages import HumanMessage,SystemMessage
from openai import base_url

#通过 python-dotenv 库读取 env 文件中的环境变量，并加载到当前运行的环境中
load_dotenv()

# 2.实例化模型
model = init_chat_model(
    model='qwen-plus',
    model_provider='openai',
    api_key=os.getenv('QWEN_API_KEY'),
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
)

async def main():
    response = await model.ainvoke("你是谁")
    print(f"响应类型是：{type(response)}")
    print(response.content)

if __name__ == "__main__":
    asyncio.run(main())

'''
LangChain 提供 ainvoke() 异步调用接口，用于在 异步环境（async/await） 中高效并行地执行模型推理。
它的核心作用是：让你同时调用多个模型请求而不阻塞主线程 —— 特别适合大批量请求或 Web 服务场景（如 FastAPI）
'''

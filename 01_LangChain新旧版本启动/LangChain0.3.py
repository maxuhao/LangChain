# LangChain0.3版本使用方式了解即可，目前还在用
# 1、导入依赖
from langchain_openai import ChatOpenAI
from openai import OpenAI
import os
from dotenv import load_dotenv

# 第一版 硬编码写死 最基础
# llm = ChatOpenAI(
#     model="qwen-plus",
#     api_key="sk-549f31001ce046a3930499f87d1c1384",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )

# 第二版 配置环境变量
# llm = ChatOpenAI(
#     model="qwen-plus",
#     api_key=os.getenv("QWEN_API_KEY"),  # 在环境变量里获取
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )

# 第三版 读取env
load_dotenv(encoding="utf-8") # 加上这段就是直接读取当前目录的.env
llm = ChatOpenAI(
    model="qwen-plus",
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 在环境变量里获取
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)



response = llm.stream("你是谁？")
for chunk in response:
    print(chunk.content, end='')

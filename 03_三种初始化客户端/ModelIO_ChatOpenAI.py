from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
'''
    封装层：LangChain 对 OpenAI API 的封装
    特点：适配 LangChain 生态系统
    适用：需要 LangChain 集成功能时
    1.0以后用init_chat_model 不用这个
'''
load_dotenv(encoding='utf-8')

chatLLM = ChatOpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    # other params...
)

# messages = [
#     {"role": "system", "con   tent": "You are a helpful assistant."},
#     {"role": "user", "content": "你是谁？"}]

messages = [
    {'role':'system','content': '你是一个专业的Java+Python+智能体后端工程师'},
    {'role':'user', 'content': '你是谁？'}
]

response = chatLLM.invoke(messages)

print(response.content)
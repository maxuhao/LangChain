# Please install OpenAI SDK first: `pip install openai`
import os

from dotenv import load_dotenv
from openai import OpenAI
'''
    原生调用：直接使用官方 openai 库
    特点：最接近原始 API 接口
    适用：需要精细控制 API 参数时
'''
load_dotenv(encoding='utf-8')
client = OpenAI(
    api_key=os.getenv("DS_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello,你是谁"},
    ],
    stream=False
)

print(response.choices[0].message.content)
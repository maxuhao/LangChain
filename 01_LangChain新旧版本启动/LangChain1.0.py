# LangChain1.0+版本使用方式 目前主流

# 1、导入依赖
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 2、实例化模型
load_dotenv(encoding='utf-8')
model = init_chat_model(
    model='qwen-plus',
    # model_provider='openai',
    api_key=os.getenv("QWEN_API_KEY"),  # 在环境变量里获取
    base_url=os.getenv("QWEN_BASE_URL")
)

print(model.invoke("你是谁").content)
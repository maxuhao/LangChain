# 1.导入依赖
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
'''
    通用初始化器：LangChain 的通用模型工厂函数
    特点：自动根据参数选择合适的模型类
    适用：希望简化模型初始化过程的场景
    推荐使用 init_chat_model，这是LangChain 1.0版本后官方推荐的标准做法
'''
# 2.实例化模型
load_dotenv(encoding='utf-8')
model = init_chat_model(
    model="deepseek-chat",
    api_key=os.getenv("DS_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 3.调用模型
print(model.invoke("你是谁").content)
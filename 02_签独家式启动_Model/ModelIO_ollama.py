from langchain_ollama import ChatOllama
from dotenv import load_dotenv
'''
pip install -qU langchain-ollama
pip install -U ollama
'''

load_dotenv()
# 调用本地ollama
model = ChatOllama(
    model="qwen3:0.6b",
    base_url="http://127.0.0.1:11434",
)
async def run():
    async for chunk in  model.astream("你是一位专业的Java后端讲师，分别总结出Java9-11新特性、Java12-17新特性、Java18-21新特性、Java22-25新特性"):
        print(chunk.content, end="", flush=True)


if __name__ == "__main__":
    import asyncio
    asyncio.run(run())



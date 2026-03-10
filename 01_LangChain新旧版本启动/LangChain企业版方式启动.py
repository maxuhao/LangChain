#导入必要的库
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.exceptions import LangChainException

#加载env文件中的环境变量
load_dotenv(encoding='utf-8')

#配置日志（可选，便于调试）
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def init_llm_client() -> ChatOpenAI:

    # 读取环境变量并做非空校验
    api_key = os.getenv('DASHSCOPE_API_KEY')
    if not api_key:
        raise ValueError("环境变量 QWEN_API_KEY 未配置，请检查.env文件")

    # 初始化LLM客户端
    llm = ChatOpenAI(
        model='qwen-plus',
        api_key=api_key,
        base_url=os.getenv("DASHSCOPE_BASE_URL"),
        temperature=0.7,
        max_tokens=2048
    )
    return llm



def main():
    try:
        #初始化客户端
        llm = init_llm_client()
        logger.info("LLM初始化成功")

        # 调用模型
        response = llm.invoke("你是谁？")
        logger.info(response.content)

        restream = llm.stream("你会什么？")
        for res in restream:
            print(res.text, end='')

    except LangChainException as e:
        logger.error(f"模型调用失败：{str(e)}")



if __name__ == '__main__':
    main()


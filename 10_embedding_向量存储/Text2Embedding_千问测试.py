# https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587
import os

import dashscope
from http import HTTPStatus

input_text = "衣服的质量杠杠的"

resp = dashscope.TextEmbedding.call(
    api_key=os.getenv("aliQwen-api"),
    model="text-embedding-v4",
    input=input_text,
)

if resp.status_code == HTTPStatus.OK:
    print(resp)



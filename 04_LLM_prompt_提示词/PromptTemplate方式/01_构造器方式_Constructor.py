import os

from langchain.chat_models import init_chat_model
# 方式1：使用构造方法实例化提示词模板
from langchain_core.prompts import PromptTemplate
from openai import api_key, base_url

'''
template：定义提示词模板的字符串，其中包含文本和变量占位符（如{name}） ；
input_variables： 列表，指定了模板中使用的变量名称，在调用模板时被替换；
partial_variables：字典，用于定义模板中一些固定的变量名。这些值不需要再每次调用时被替换。
'''

# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 该模板包含两个变量：role（角色）和question（问题） ：等于在字符串里写了变量，需要对应的在input_variables在定义此对象
template = PromptTemplate(
    template='你是一个{role}工程师，请回答我的问题给出答案，我的问题是：{question} ',
    input_variables=['role','question']
)

# 示例1
# 使用模板格式化具体的提示词内容
# 将role替换为"python开发"，question替换为"冒泡排序怎么写？"
prompt = template.format(role='Python工程师',question='冒泡排序怎么写，只要代码不要其他，简洁')

#输出格式化后的提示词内容
print(prompt) # 你是一个Python工程师工程师，请回答我的问题给出答案，我的问题是：冒泡排序怎么写，只要代码不要其他，简洁



model = init_chat_model(
    model='qwen-plus',
    model_provider='openai',
    api_key=os.getenv('aliQwen-api'),
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
)

response = model.invoke(prompt)
print(response.content)
print()


#示例2
template = PromptTemplate(
    template='请评价{product}的优缺点，包括{aspect1}和{aspect2}',
    input_variables=['product','aspect1','aspect2']
)


prompt1 = template.format(product='智能手机',aspect1='电池续航',aspect2='拍照质量')
prompt2 = template.format(product='笔记本电脑',aspect1='处理速度',aspect2='便捷性')

print(prompt1)
print(prompt2)







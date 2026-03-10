# 方式2：使用 from_template 方法实例化提示词模板
from langchain_core.prompts import PromptTemplate

'''
template：定义提示词模板的字符串，其中包含文本和变量占位符（如{name}） ；
input_variables： 列表，指定了模板中使用的变量名称，在调用模板时被替换；
partial_variables：字典，用于定义模板中一些固定的变量名。这些值不需要再每次调用时被替换。
'''

# 示例1
# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 模板包含两个占位符：{role}表示角色，{question}表示问题
template = PromptTemplate.from_template("你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")

# 使用指定的角色和问题参数来格式化模板，生成最终的提示词字符串
# role: 工程师角色描述
# question: 具体的技术问题是
prompt = template.format(role='Python开发',question='快速排序怎么写')


#输出提示词
print(prompt)


#示例2
template = PromptTemplate.from_template('请给我一个关于{topic}的{type}解释。')
prompt = template.format(topic='量子力学',type='详细')
print(prompt)


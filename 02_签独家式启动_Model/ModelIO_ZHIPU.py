from langchain_community.chat_models import ChatZhipuAI
from langchain.messages import AIMessage, HumanMessage, SystemMessage



import os

os.environ["ZHIPUAI_API_KEY"] = "zhipuai_api_key"

chat = ChatZhipuAI(
    model="glm-4",
    temperature=0.5,
)


messages = [
    AIMessage(content="Hi."),
    SystemMessage(content="Your role is a poet."),
    HumanMessage(content="Write a short poem about AI in four lines."),
]

response = chat.invoke(messages)
print(response.content)  # Displays the AI-generated poem



print("*" * 60)


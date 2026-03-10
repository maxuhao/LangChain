
from langchain.tools import tool

@tool(description="两数相加")
def add(x: int, y: int) -> int:
    return x + y


result = add.invoke({'x':30, 'y':10})

print(result)

print()

print(f"{add.name=}\n{add.description=}\n{add.args=}")

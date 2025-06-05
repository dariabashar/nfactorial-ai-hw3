import os
from dotenv import load_dotenv
import requests
from langchain_openai import ChatOpenAI

load_dotenv()

user_input = input("Введите запрос: ")
a2a_payload = {
    "sender": "LangChainAgent",
    "receiver": "LlamaIndexAgent",
    "content": user_input
}
# llm = ChatOpenAI()
# response = llm.invoke("Hi! I'm here to talk to you")
# print(response)

try:
    response = requests.post("http://localhost:5001/analyze", json=a2a_payload)
    response.raise_for_status()
    result = response.json()
    print(f"Answer from {result['sender']}:\n{result['content']}")
except Exception as e:
    print("Something went wrong: ", e)
import os
<<<<<<< HEAD
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
=======
from fastapi import FastAPI, Request
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool
# from llama_index.workflow.base import WorkflowRunner, WorkflowOutput
from llama_index.core import Settings
from dotenv import load_dotenv
import uvicorn

load_dotenv()
from llama_index.llms.openai import OpenAI
Settings.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI()
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
@app.post("/analyze")
async def analyze(request: Request):
    a2a_payload = await request.json()
    content = a2a_payload.get("content","")
    sender = a2a_payload.get("sender","uknown")
    print(f"Got the message from {sender}: {content}")

    response = query_engine.query(content)

    return {
        "sender": "LlamaIndexAgent",
        "receiver": sender,
        "content": str(response),
        "metadata":{
            "original_query": content
        }
    }
if __name__ == "__main__":
    uvicorn.run("main:app",port=5001, reload=True)
>>>>>>> 504f9aa (Initial commit)

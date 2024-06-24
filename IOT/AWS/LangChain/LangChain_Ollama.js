#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

# model
#llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
llm = ChatOllama(model="EEVE-Korean-Instruct-8B:latest")

# chain 실행
llm.invoke("지구의 자전 주기는?")

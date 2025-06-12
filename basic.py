
import getpass
import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate

load_dotenv()
cohere_api_key = os.getenv("secret_key")
llm = ChatCohere(model="command-r-plus", cohere_api_key=cohere_api_key )


response=llm.invoke("Hi")
print(response.content)
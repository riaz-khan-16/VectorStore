
import getpass
import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate

load_dotenv()
cohere_api_key = os.getenv("secret_key")
llm = ChatCohere(model="command-r-plus", cohere_api_key=cohere_api_key )


response=llm.stream("wrtie a paragraph about Data structure and Algorithms of 20000 words")
for res in response:
    print(res.content, end='', flush=True)
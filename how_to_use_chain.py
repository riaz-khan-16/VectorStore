


import getpass
import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()
cohere_api_key = os.getenv("secret_key")
llm = ChatCohere(model="command-r-plus", cohere_api_key=cohere_api_key )

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain the concept of {topic} in simple terms."
)

chain=LLMChain(llm=llm, prompt=prompt)
result = chain.invoke({"topic": "blockchain"})

print(result)
import getpass
import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
load_dotenv()
cohere_api_key = os.getenv("secret_key")
llm = ChatCohere(model="command-r-plus", cohere_api_key=cohere_api_key )

# history=ChatMessageHistory()
# history.add_user_message("Hi! I am Riaz")
# history.add_ai_message("Hello! Whats Up?")

# print(history)

memory=ConversationBufferMemory()
conversation=ConversationChain(llm=llm, memory=memory)
conversation.predict(input="Hi")
conversation.predict(input="Who is ATM AZHARUL ISLAM in Bangladesh")

print(memory.buffer)
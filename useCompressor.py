
import getpass
import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_cohere import ChatCohere


load_dotenv()
cohere_api_key = os.getenv("secret_key")

embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key=cohere_api_key  
)






documents = TextLoader("bdg.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
retriever = Chroma.from_documents(texts, embeddings).as_retriever()

# docs = retriever.invoke("Where  is Taraganj")
# print(docs[0].page_content)


from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_cohere import ChatCohere

llm = ChatCohere(model="command-r-plus", cohere_api_key=cohere_api_key  )
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)

compressed_docs = compression_retriever.invoke(
    "Where is Taraganj"
)
print(compressed_docs[0].page_content)
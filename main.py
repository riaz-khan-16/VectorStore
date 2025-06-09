
import getpass
import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma




load_dotenv()
cohere_api_key = os.getenv("secret_key")

embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key=cohere_api_key  
)



# Load the document, split it into chunks, embed each chunk and load it into the vector store.
raw_documents = TextLoader('bdg.txt').load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)


db = Chroma.from_documents(documents,embeddings)

query = "Riaz"
docs = db.similarity_search(query)
print(docs[0].page_content)


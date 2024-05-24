from dotenv import load_dotenv, find_dotenv
import os
from langchain_openai import ChatOpenAI
# langchain이 openai 에서 독립되어서 매개변수가 바뀜 (설치해야함)
from langchain.memory import ConversationSummaryBufferMemory
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnablePassthrough

loader = PyPDFLoader("./static/download/Yeo_In_Hyeop.pdf")
docs = loader.load()
print(len(docs))
print(docs[0])
exit()

# Chunk(block) 단위로 Split (쪼개기)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap= 200
)

# 임베딩 -> 형태소를 숫자로 표현
# ex) 5차원 텍스트 임베딩 (숫자 5개로 표현 한다는 뜻)
# dog : 0.3 0.7 1.5 59 32
embeddings = OpenAIEmbeddings()

cache_dir = LocalFileStore("./.cache/")
cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)
vectorstore = Chroma.from_documents(docs, cached_embeddings)

# Vector DB: Chroma 저장
directory = "./llm/chroma_db"
vector_index = Chroma.from_documents(
    docs,                               # Documents
    OpenAIEmbeddings(),                 #Text embeddings model
    persist_directory=directory         # file system (저장 경로)
)
vector_index.persist() #Save
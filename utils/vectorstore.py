#%%
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
import dotenv

dotenv.load_dotenv()

def create_vectorstore(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")  # ✅ correct
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore

def get_retriever(chunks):
    vectorstore = create_vectorstore(chunks)
    retriever = vectorstore.as_retriever()
    return retriever
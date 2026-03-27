#%%
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)
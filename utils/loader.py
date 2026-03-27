#%%
import os
from langchain_community.document_loaders import PyPDFLoader

def load_pdfs_from_folder(folder_path):
    docs = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            loader = PyPDFLoader(file_path)
            docs.extend(loader.load())

    return docs
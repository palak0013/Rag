import os
import streamlit as st
from dotenv import load_dotenv
from utils.loader import load_pdfs_from_folder
load_dotenv()
print("API KEY:", os.getenv("GOOGLE_API_KEY"))

#from utils.loader import load_pdf
from utils.splitter import split_text
from utils.vectorstore import create_vectorstore

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

file_paths = []

if uploaded_files:
    if not os.path.exists("temp_pdfs"):
        os.makedirs("temp_pdfs")

    for file in uploaded_files:
        file_path = os.path.join("temp_pdfs", file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        file_paths.append(file_path)


if file_paths:
    docs = load_pdfs_from_folder("temp_pdfs")
else:
    docs = load_pdfs_from_folder("data")  # fallback
    
'''chunks = split_text(docs)
vectorstore = create_vectorstore(chunks)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})'''

'''if st.sidebar.button("Process PDFs"):
    chunks = split_text(docs)
    vectorstore = create_vectorstore(chunks)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    st.success("PDFs processed!")'''
    
if "retriever" not in st.session_state:
    st.session_state.retriever = None

if st.sidebar.button("Process PDFs"):
    chunks = split_text(docs)
    vectorstore = create_vectorstore(chunks)
    st.session_state.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

'''while True:
    query = st.text_input("Ask something:")
    if query.lower() == 'exit':
        break
    docs = retriever.invoke(query)

    # 👉 THIS IS YOUR CONTEXT
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a helpful assistant.

    Answer ONLY using the provided context.
    
    Give a well-structured answer with:
   - Headings
   - Bullet points
   - Clean formatting
   
    If the answer is not in the context, say:
   "I don't know based on the provided document."

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    print("\n🧠 Answer:\n")
    print(response.content.strip())

    #print(response.content)

    #print("Vector DB created successfully ✅")
    #print("Retrieved chunks:\n", docs)
    #print("Total chunks:", len(chunks))
    #print(chunks[0].page_content[:500])'''
    
query = st.text_input("Ask something:")

if query and st.session_state.retriever:
    docs = st.session_state.retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a helpful assistant.

    Answer ONLY using the provided context.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    try:
        st.write(response.content)
    except:
        st.write(response)

import streamlit as st
from utils.rag import rag_pipeline
from utils.vectorstore import get_retriever
from utils.loader import load_pdfs_from_folder as load_documents
from utils.splitter import split_text as split_documents
from models import client

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="PDF RAG App", layout="wide")

st.title("📄 Chat with your PDFs")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Controls")

    load_data = st.button("📥 Load PDFs")
    clear_chat = st.button("🧹 Clear Chat")
    show_sources = st.checkbox("📚 Show Sources")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state or clear_chat:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None

# ---------------- LOAD DATA ----------------
if load_data:
    with st.spinner("Processing PDFs..."):

        docs = load_documents("data")   # your data folder
        chunks = split_documents(docs)
        retriever = get_retriever(chunks)

        st.session_state.retriever = retriever

    st.success("✅ PDFs loaded successfully!")

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- CHAT INPUT ----------------
query = st.chat_input("Ask something from your PDFs...")

if query:
    if st.session_state.retriever is None:
        st.warning("⚠️ Please load PDFs first!")
    else:
        # Store user message
        st.session_state.messages.append({"role": "user", "content": query})

        with st.chat_message("user"):
            st.write(query)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                response, docs = rag_pipeline(
                    query,
                    st.session_state.retriever,
                    client
                )

                st.write(response)

                # Show sources
                if show_sources:
                    st.markdown("### 📚 Retrieved Chunks")
                    for doc in docs[:3]:
                        st.markdown(f"- {doc.page_content[:200]}...")

        # Store assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
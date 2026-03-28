# 📄 AI-Powered PDF Chatbot (RAG)

An interactive AI chatbot that allows users to ask questions from multiple PDFs using Retrieval-Augmented Generation (RAG).

---

## 🚀 Live Demo
🔗 [Add your deployed app link here]

---

## 📌 Features

- 📄 Chat with multiple PDFs
- 🔍 Semantic search using vector database (Chroma)
- 🧠 Context-aware answers using LLM (Google Gemini)
- 💬 Chat-style UI using Streamlit
- 📚 Source-based answers (retrieved chunks shown)
- ⚡ Fast and efficient retrieval pipeline

---

## 🧠 How It Works

1. PDFs are loaded and processed  
2. Text is split into chunks  
3. Embeddings are created using Gemini Embeddings  
4. Chunks are stored in a vector database (Chroma)  
5. User query is matched with relevant chunks  
6. LLM generates answer using retrieved context  

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM:** Google Gemini (gemini-2.5-flash)  
- **Embeddings:** Gemini Embeddings  
- **Vector DB:** Chroma  
- **Framework:** LangChain  

---



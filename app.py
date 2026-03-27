import os
from dotenv import load_dotenv
from utils.loader import load_pdfs_from_folder
load_dotenv()
print("API KEY:", os.getenv("GOOGLE_API_KEY"))

#from utils.loader import load_pdf
from utils.splitter import split_text
from utils.vectorstore import create_vectorstore

docs = load_pdfs_from_folder("data")
chunks = split_text(docs)
vectorstore = create_vectorstore(chunks)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

while True:
    query = input("\nAsk something(or type 'exit' to quit): ")
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
    #print(chunks[0].page_content[:500])

def rag_pipeline(query, retriever, client):
    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a helpful assistant.
    Answer ONLY using the provided context.

    Give a well-structured answer with:
    - Headings
    - Bullet points

    Context:
    {context}

    Question:
    {query}
    """

    #response = llm.invoke(prompt)

    #return response.content, docs
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

    return response.text, docs
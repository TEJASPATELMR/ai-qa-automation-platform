import ollama
import numpy as np

def query_rag(question, index, docs):

    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=question
    )

    query_vector = np.array([response["embedding"]]).astype("float32")

    D, I = index.search(query_vector, k=3)

    context = ""

    for i in I[0]:
        context += docs[i].page_content + "\n"

    prompt = f"""
You are a QA engineer.

Based on the following requirement:

{context}

Generate detailed test cases.
"""

    result = ollama.chat(
        model="deepseek-coder",
        messages=[{"role": "user", "content": prompt}]
    )

    return result["message"]["content"]
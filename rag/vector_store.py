import faiss
import numpy as np
import ollama

def create_vector_store(docs):

    embeddings = []

    for doc in docs:

        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=doc.page_content
        )

        embeddings.append(response["embedding"])

    embeddings = np.array(embeddings).astype("float32")

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, docs
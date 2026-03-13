from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings


def retrieve_docs(query):

    embeddings = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    docs = db.similarity_search(query, k=3)

    return docs
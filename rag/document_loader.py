import os
from docx import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents():

    docs = []

    folder = "data/requirements"

    for file in os.listdir(folder):
        if file.endswith(".docx"):

            path = os.path.join(folder, file)

            doc = Document(path)

            text = ""

            for para in doc.paragraphs:
                text += para.text + "\n"

            docs.append(text)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.create_documents(docs)

    return chunks
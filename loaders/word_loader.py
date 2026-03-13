from docx import Document

def load_word_document(path):

    doc = Document(path)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)
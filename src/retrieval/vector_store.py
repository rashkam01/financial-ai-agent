from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def create_vector_store(chunks):

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory="storage/vector_db"
    )

    return vector_db

def load_vector_store():

    vector_db = Chroma(
        persist_directory="storage/vector_db",
        embedding_function=OpenAIEmbeddings()
    )

    return vector_db
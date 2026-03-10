import sys
import os

from dotenv import load_dotenv
load_dotenv()
print("API KEY FOUND:", os.getenv("OPENAI_API_KEY")[:10])

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingestion.pdf_ingestion import load_pdfs, split_documents
from src.retrieval.vector_store import create_vector_store


DATA_PATH = "data/raw"


def run():

    all_documents = []

    for file in os.listdir(DATA_PATH):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(DATA_PATH, file)

            documents = load_pdfs(pdf_path)

            all_documents.extend(documents)

    chunks = split_documents(all_documents)

    create_vector_store(chunks)

    print("Vector database created successfully.")


if __name__ == "__main__":
    run()
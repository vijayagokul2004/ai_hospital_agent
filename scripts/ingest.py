from app.rag.loader import load_hospital_documents
from app.rag.chunker import split_documents
from app.rag.vectorstore import create_vector_store


def ingest_documents():
    print("Loading documents...")

    documents = load_hospital_documents()

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Total chunks: {len(chunks)}")

    print("Creating Qdrant collection and storing documents...")

    create_vector_store(chunks)

    print("Documents successfully stored in Qdrant!")


if __name__ == "__main__":
    ingest_documents()
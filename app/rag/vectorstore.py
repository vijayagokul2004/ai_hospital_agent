from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from app.rag.embeddings import get_embedding_model

COLLECTION_NAME = "hospital_documents"
QDRANT_PATH = "data/qdrant"


def create_vector_store(documents):
    embeddings = get_embedding_model()

    vector_store = QdrantVectorStore.from_documents(
        documents,
        embedding=embeddings,
        path=QDRANT_PATH,
        collection_name=COLLECTION_NAME,
    )

    return vector_store


def get_vector_store():
    embeddings = get_embedding_model()

    client = QdrantClient(path=QDRANT_PATH)

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )

    return vector_store
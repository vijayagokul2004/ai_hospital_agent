from app.rag.vectorstore import get_vector_store


def search_hospital(query: str, k: int = 5):
    vector_store = get_vector_store()

    results = vector_store.similarity_search(query, k=k)

    return results


if __name__ == "__main__":
    query = "What are the cardiology department timings?"

    results = search_hospital(query)

    print(f"Found {len(results)} results")

    for i, document in enumerate(results, start=1):
        print(f"\n--- RESULT {i} ---")
        print(document.page_content)
        print("Metadata:", document.metadata)
        
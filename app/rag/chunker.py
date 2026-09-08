from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.loader import load_hospital_documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
        length_function=len,
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks


if __name__ == "__main__":
    documents = load_hospital_documents()
    chunks = split_documents(documents)

    for i, chunk in enumerate(chunks[:3]):
        print(f"\n--- CHUNK {i + 1} ---")
        print(chunk.page_content)
        print("\nMetadata:", chunk.metadata)
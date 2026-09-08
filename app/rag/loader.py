from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


PDF_PATH = Path("data/documents/hospital_information.pdf")


def load_hospital_documents():
    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    return documents


if __name__ == "__main__":
    documents = load_hospital_documents()

    for document in documents[:2]:
        print("\n--- PAGE ---")
        print(document.page_content[:500])
        print("Metadata:", document.metadata)
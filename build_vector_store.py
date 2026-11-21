from src.ingestion import load_documents
from src.chunking import split_into_chunks
from src.vector_store import create_vector_store, save_vector_store


def main():
    print("Step 1: Loading hotel documents...")
    documents = load_documents()

    if not documents:
        raise ValueError("No documents found in the knowledge base.")

    print(f"Loaded {len(documents)} documents.")

    print("Step 2: Splitting documents into chunks...")
    chunks = split_into_chunks(documents)

    if not chunks:
        raise ValueError("No chunks were generated.")

    print(f"Created {len(chunks)} chunks.")

    print("Step 3: Creating FAISS vector store...")
    vector_store = create_vector_store(chunks)

    print("Step 4: Saving FAISS vector store...")
    save_vector_store(vector_store)

    print("FAISS initialization completed successfully!")


if __name__ == "__main__":
    main()
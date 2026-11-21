from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model
from src.ingestion import load_documents
from src.chunking import split_into_chunks
from config import VECTOR_STORE_PATH
import os


def create_vector_store(chunks):
    """Embed each chunk and build a searchable Faiss index in memory."""

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store


def save_vector_store(vector_store):
    """Save the FAISS vector store permanently."""

    os.makedirs(VECTOR_STORE_PATH, exist_ok=True)

    vector_store.save_local(VECTOR_STORE_PATH)

    print("FAISS vector store saved successfully!")


def load_vector_store():
    """Load an existing FAISS vector store from disk."""

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("FAISS vector store loaded successfully!")

    return vector_store


def get_or_create_vector_store():
    """Load an existing FAISS index or create a new one."""

    index_file = os.path.join(VECTOR_STORE_PATH, "index.faiss")

    if os.path.exists(index_file):

        print("Existing FAISS index detected. Loading...")
        vector_store = load_vector_store()

    else:

        print("No existing FAISS index found.")
        print("Loading hotel documents...")

        documents = load_documents()

        if not documents:
            raise ValueError("No documents found in the knowledge base.")

        print(f"Loaded {len(documents)} documents.")

        print("Splitting documents into chunks...")

        chunks = split_into_chunks(documents)

        if not chunks:
            raise ValueError("No chunks were generated.")

        print(f"Created {len(chunks)} chunks.")

        print("Creating FAISS vector store...")

        vector_store = create_vector_store(chunks)

        print("Saving FAISS vector store...")

        save_vector_store(vector_store)

    return vector_store
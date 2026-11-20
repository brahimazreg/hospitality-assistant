from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model
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
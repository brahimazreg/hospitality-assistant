from src.vector_store import load_vector_store
from config import TOP_K_RESULT


# Load FAISS once when this module is imported
vector_store = load_vector_store()


def retrieve_documents(question):
    """Retrieve the most relevant documents for a user question."""

    results = vector_store.similarity_search(
        query=question,
        k=TOP_K_RESULT
    )

    return results
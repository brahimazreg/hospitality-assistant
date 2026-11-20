
import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from config import EMBEDDING_MODEL_NAME

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")


def get_embedding_model():
    """Initialize the Cohere embedding model."""

    if not COHERE_API_KEY:
        raise ValueError("Missing COHERE_API_KEY in .env file")

    embeddings = CohereEmbeddings(
        model=EMBEDDING_MODEL_NAME,
        cohere_api_key=COHERE_API_KEY
    )

    return embeddings


def embeddings_chunks(chunks):
    """Convert document chunks into numerical vectors."""

    embeddings = get_embedding_model()

    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors
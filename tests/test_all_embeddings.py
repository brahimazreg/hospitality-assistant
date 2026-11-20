from src.ingestion import load_documents
from src.chunking import split_into_chunks
from src.embeddings import get_embedding_model

# Load and split hotel documents
documents = load_documents()
chunks = split_into_chunks(documents)

# Generate embeddings
embeddings = get_embedding_model()
texts = [chunk.page_content for chunk in chunks]
vectors = embeddings.embed_documents(texts)

# Validate results
print("Number of chunks:", len(chunks))
print("Number of vectors:", len(vectors))
print("Vector dimensions:", len(vectors[0]))

assert len(chunks) == len(vectors)
assert all(len(vector) == 1024 for vector in vectors)

print("All embedding checks passed!")
from src.vector_store import load_vector_store

# Load the existing FAISS index
vector_store = load_vector_store()

# Check the number of stored vectors
print("FAISS index size:", vector_store.index.ntotal)

assert vector_store.index.ntotal == 7

print("FAISS loading test passed!")
from src.ingestion import load_documents
from src.chunking import split_into_chunks
from src.vector_store import create_vector_store, save_vector_store

documents = load_documents()
chunks = split_into_chunks(documents)

vector_store = create_vector_store(chunks)

print("Number of chunks:", len(chunks))
print("FAISS index size:", vector_store.index.ntotal)

assert vector_store.index.ntotal == len(chunks)

save_vector_store(vector_store)

print("FAISS test passed!")
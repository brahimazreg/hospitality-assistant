from src.ingestion import load_documents
from src.chunking import split_into_chunks


documents = load_documents()
chunks = split_into_chunks(documents)

print("Total original documents:", len(documents))
print("Total chunks generated:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}")
    print("Source:", chunk.metadata.get("source"))
    print("Content:", chunk.page_content)
print("\n--- CHUNK SIZE VALIDATION ---")

for i, chunk in enumerate(chunks):
    print(
        f"Chunk {i + 1}: "
        f"{len(chunk.page_content)} characters"
    )
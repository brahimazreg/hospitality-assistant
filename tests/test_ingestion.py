from src.ingestion import load_documents

documents = load_documents()

print("Total extracted documents:", len(documents))

for i, doc in enumerate(documents):
    print(f"\nDocument {i + 1}")
    print("Source:", doc.metadata.get("source"))
    print("Content:", doc.page_content[:200])
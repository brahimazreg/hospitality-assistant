from src.retriever import retrieve_documents

questions = [
    "What time does breakfast start?",
    "À quelle heure commence le petit-déjeuner ?",
    "متى يبدأ الإفطار؟"
]

for question in questions:
    print("\nQuestion:", question)

    results = retrieve_documents(question)

    for i, document in enumerate(results):
        print(f"\nResult {i + 1}:")
        print("Content:", document.page_content)
        print("Source:", document.metadata.get("source"))
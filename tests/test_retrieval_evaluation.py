from src.retriever import retrieve_documents


evaluation_cases = [
    {
        "question": "What time does breakfast start?",
        "expected_keyword": "06:30",
        "expected_source": "hotel_services.docx",
    },
    {
        "question": "À quelle heure commence le petit-déjeuner ?",
        "expected_keyword": "06:30",
        "expected_source": "hotel_services.docx",
    },
    {
        "question": "متى يبدأ الإفطار؟",
        "expected_keyword": "06:30",
        "expected_source": "hotel_services.docx",
    },
    {
        "question": "What time is check-in?",
        "expected_keyword": "14:00",
        "expected_source": "hotel_policy.pdf",
    },
    {
        "question": "When does the swimming pool close?",
        "expected_keyword": "20:00",
        "expected_source": "hotel_services.docx",
    },
    {
        "question": "What is the cancellation policy?",
        "expected_keyword": "48",
        "expected_source": "hotel_policy.pdf",
    },
]


for case in evaluation_cases:
    question = case["question"]
    expected_keyword = case["expected_keyword"]
    expected_source = case["expected_source"]

    results = retrieve_documents(question)

    print("\n" + "=" * 60)
    print("Question:", question)
    print("Expected source:", expected_source)
    print("Expected keyword:", expected_keyword)

    found = False

    for rank, document in enumerate(results, start=1):
        content = document.page_content
        source = document.metadata.get("source", "")

        keyword_found = expected_keyword in content
        source_matches = expected_source in source

        if keyword_found and source_matches:
            found = True

        print(f"\nResult {rank}")
        print("Source:", source)
        print("Expected keyword found:", keyword_found)
        print("Expected source matched:", source_matches)
        print("Content:", content[:250])

    print("\nEvaluation:", "PASS" if found else "REVIEW")
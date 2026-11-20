from src.generator import answer_question


def test_rag():

    questions = [
        "What time does breakfast start?",
        "À quelle heure commence le petit-déjeuner ?",
        "متى يبدأ الإفطار؟",
        "What is the price of a room per night?"
    ]

    for question in questions:

        answer = answer_question(question)

        print("\n" + "=" * 60)
        print("Question:", question)
        print("Answer:", answer)

        assert answer


if __name__ == "__main__":
    test_rag()
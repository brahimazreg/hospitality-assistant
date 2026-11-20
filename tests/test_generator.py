from src.generator import get_llm


def test_groq_model():
    llm = get_llm()

    response = llm.invoke(
        "Answer in one sentence: What is the purpose of a hotel reception?"
    )

    print("\nGroq model response:")
    print(response.content)

    assert response.content


if __name__ == "__main__":
    test_groq_model()
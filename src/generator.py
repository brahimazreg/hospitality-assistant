from langchain_groq import ChatGroq
from config import LLM_MODEL_NAME, PROMPT
from dotenv import load_dotenv
import os
from src.retriever import retrieve_documents

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def get_llm():
    """Initialize the Groq language model."""

    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY in .env file")

    llm = ChatGroq(
        model=LLM_MODEL_NAME,
        groq_api_key=GROQ_API_KEY,
        temperature=0
    )

    return llm


def format_context(documents):
    """Combine document content and source information."""

    context_parts = []

    for document in documents:
        source = os.path.basename(
            document.metadata.get("source", "Unknown source")
        )

        context_parts.append(
            f"Source: {source}\n"
            f"Content: {document.page_content}"
        )

    context = "\n\n".join(context_parts)

    return context


def generate_answer(question, documents):
    """Generate an answer using the retrieved documents."""

    llm = get_llm()

    context = format_context(documents)

    prompt = PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content


def answer_question(question):
    """Retrieve relevant documents and generate an answer."""

    documents = retrieve_documents(question)

    answer = generate_answer(question, documents)

    return answer
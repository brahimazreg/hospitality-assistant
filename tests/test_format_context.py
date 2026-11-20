from src.retriever import retrieve_documents
from src.generator import format_context

documents = retrieve_documents("What time does breakfast start?")

print(format_context(documents))
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

# LLM model
LLM_MODEL_NAME="openai/gpt-oss-120b"

EMBEDDING_MODEL_NAME = "embed-multilingual-v3.0"

# path vector store
VECTOR_STORE_PATH=os.path.join("data","faiss_index")

# path data file
PATH_DATA_FILE = os.path.join("data", "knowledge_base")

# Top result
TOP_K_RESULT=3

# chunks
CHUNK_SIZE=500
CHUNK_OVERLAP=50

PROMPT = """
You are an AI assistant specialized in answering questions
about a hotel using the provided documents.

Instructions:
- Use only the information provided in the context.
- Do not use your general knowledge to answer hotel-related questions.
- Do not invent or assume information.
- If the answer is not available in the context, clearly state
  that you cannot find the answer in the provided documents.
- Always answer in the same language as the user's question:
  English, French, or Arabic.
- Keep your answers clear, helpful, and professional.
- At the end of your answer, mention the source filename(s)
  used to answer the question.
- Only cite filenames explicitly provided in the context.
  Never invent source filenames.

Context:
{context}

Question:
{question}

Answer:
"""

# Check if GIMINI_API_KEY is missing
def check_api_key():
    """ stop early with a clear message if required key is missing"""
    if not GEMINI_API_KEY:
        raise ValueError("Missing GIMINI_API_KEY  please added it to your .env file")
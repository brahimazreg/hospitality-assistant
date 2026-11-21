from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.generator import answer_question

app = FastAPI(
    title="Oman Hospitality AI Assistant",
    description="A multilingual AI assistant for hotel information.",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Oman Hospitality AI Assistant API is running!"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        answer = answer_question(request.question)

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(q: Query):
    # placeholder, will connect to RAG pipeline soon
    return {"answer": "This endpoint will serve chatbot responses soon."}

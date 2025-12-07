from fastapi import APIRouter
from pydantic import BaseModel
from app.core.db import SessionLocal
from app.models.document import Document
from app.services.retriever import Retriever
import json

router = APIRouter()
retriever = Retriever()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask(req: AskRequest):
    db = SessionLocal()
    docs = db.query(Document).all()
    chunks = []
    for d in docs:
        pages = json.loads(d.pages)
        for p in pages:
            chunks.append({"doc_id": d.id, "page": p["page"], "text": p["text"][:2000]})
    retriever.index(chunks)
    hits = retriever.query(req.question, top_k=4)
    answer = " ".join([h['text'][:500] for h in hits])
    citations = [{"doc_id": h["doc_id"], "page": h["page"], "score": h["score"]} for h in hits]
    db.close()
    return {"answer": answer, "citations": citations}

from fastapi import APIRouter
from pydantic import BaseModel
from app.core.db import SessionLocal
from app.models.document import Document
from app.services.extractor import extract_parties, extract_effective_date, extract_governing_law, extract_auto_renewal
import json

router = APIRouter()

class ExtractRequest(BaseModel):
    document_id: int

@router.post("/extract")
def extract(req: ExtractRequest):
    db = SessionLocal()
    doc = db.query(Document).filter(Document.id == req.document_id).first()
    if not doc:
        return {"error": "document not found"}
    pages = json.loads(doc.pages)
    text = doc.text
    res = {
        "parties": extract_parties(text),
        "effective_date": extract_effective_date(text),
        "governing_law": extract_governing_law(text),
        "auto_renewal": extract_auto_renewal(text),
        "term": None, "payment_terms": None,
        "termination": None, "confidentiality": None, "indemnity": None,
        "liability_cap": None, "signatories": []
    }
    db.close()
    return res

from fastapi import APIRouter
from pydantic import BaseModel
from app.core.db import SessionLocal
from app.models.document import Document
from app.services.extractor import extract_auto_renewal
import json, re

router = APIRouter()

class AuditRequest(BaseModel):
    document_id: int

@router.post("/audit")
def audit(req: AuditRequest):
    db = SessionLocal()
    doc = db.query(Document).filter(Document.id == req.document_id).first()
    if not doc:
        return {"error":"document not found"}
    text = doc.text
    findings = []
    ar = extract_auto_renewal(text)
    if ar.get("found"):
        ndays = ar.get("notice_days")
        severity = "medium"
        if ndays is None or (isinstance(ndays, int) and ndays < 30):
            severity = "high"
        findings.append({
            "title":"Auto-renewal clause",
            "severity": severity,
            "evidence": "auto-renew phrase"
        })
    if re.search(r"(unlimited liability|no limit to liability|no cap on liability)", text, re.IGNORECASE):
        findings.append({"title":"Unlimited liability detected","severity":"high","evidence":"matching phrase"})
    if re.search(r"(indemnif(y|ication).{0,60}(including|without limitation))", text, re.IGNORECASE|re.DOTALL):
        findings.append({"title":"Broad indemnity terms","severity":"medium","evidence":"matching phrase"})
    db.close()
    return {"findings": findings}

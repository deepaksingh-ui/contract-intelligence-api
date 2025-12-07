from fastapi import APIRouter, UploadFile, File
from app.core.db import SessionLocal
from app.models.document import Document
from app.services.pdf_loader import extract_text_by_page, pages_to_json
import shutil, os, uuid, json

router = APIRouter()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/ingest")
async def ingest(files: list[UploadFile] = File(...)):
    db = SessionLocal()
    ids = []
    for f in files:
        fname = f"{uuid.uuid4().hex}_{f.filename}"
        path = os.path.join(UPLOAD_DIR, fname)
        with open(path, "wb") as out:
            shutil.copyfileobj(f.file, out)
        pages = extract_text_by_page(path)
        doc = Document(filename=f.filename, text="\n".join(pages), pages=pages_to_json(pages))
        db.add(doc)
        db.commit()
        db.refresh(doc)
        ids.append(doc.id)
    db.close()
    return {"document_ids": ids}

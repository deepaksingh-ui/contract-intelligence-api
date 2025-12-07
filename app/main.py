from fastapi import FastAPI
from app.api import ingest, extract, ask, audit
from app.core.db import Base, engine
from app.models import document as docmod

app = FastAPI(title="Contract Intelligence ")

# create DB
Base.metadata.create_all(bind=engine)

app.include_router(ingest.router, prefix="")
app.include_router(extract.router, prefix="")
app.include_router(ask.router, prefix="")
app.include_router(audit.router, prefix="")

@app.get("/healthz")
def health():
    return {"status":"ok"}

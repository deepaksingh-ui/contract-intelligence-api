📘 Contract Intelligence API

AI-powered contract analysis system that extracts clauses, identifies risks, audits compliance, and performs semantic search on legal documents.

## 🚀 Features

Contract Clause Extraction (Dates, Parties, Payment Terms, Obligations etc.)

Risk Assessment using LLM

Contract Audit via NLP/AI

Semantic Search inside uploaded documents

AI-based Q/A (Ask anything about contract)

Fully Dockerized for easy deployment

FastAPI + Python + OpenAI models

## 🗂 Project Structure
contract-intelupdate/
│── app/
│   ├── api/
│   │   ├── ask.py
│   │   ├── audit.py
│   │   ├── extract.py
│   │   ├── search.py
│   ├── core/
│   │   ├── config.py
│   │   └── utils.py
│   ├── main.py
│
│── prompts/
│── uploads/
│── DESIGN.md
│── README.md
│── Dockerfile
│── docker-compose.yml
│── requirements.txt

## 🛠 Tech Stack
Component	Technology
Backend	FastAPI
AI Models	OpenAI / GPT-4
Containerization	Docker, Docker Compose
Language	Python 3.10+
API Docs	Swagger UI
# ⚡ How to Run the Project (Local + Docker)
### ▶ Option A — Run with Docker (Recommended)
1️⃣ Build & Start
docker-compose up --build

2️⃣ Open API Docs
http://localhost:8000/docs

3️⃣ Stop server
CTRL + C

### ▶ Option B — Run Locally (Without Docker)
Install dependencies
pip install -r requirements.txt

Run server
uvicorn app.main:app --reload


API Runs at:

http://127.0.0.1:8000/docs

# 🧪 API Endpoints (Summary)
Endpoint	Type	Description
/extract	POST	Extract key information from contract
/audit	POST	Audit the entire contract for compliance
/search	POST	Semantic search inside contract
/ask	POST	Ask AI any question about contract
/ingest	POST	Upload contract documents

# 📄 Project Design Document

See DESIGN.md for:

System Architecture

Flow Diagram

Module Breakdown

LLM Interaction Logic

# 📦 Deployment Ready

This project is fully containerized and ready for deployment on:

AWS EC2

Azure

Heroku

Render

Docker Hub

# 👨‍💻 Author

Deepak Singh
FastAPI • AI • ML • Docker Developer



















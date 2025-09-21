# 🧑‍💼 AI Resume → Job Match System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

> An end-to-end **AI-powered job matcher** that takes a resume (PDF or text), extracts its content, and finds the most relevant job postings using **Sentence-BERT embeddings** and **semantic similarity search**.

---

## ✨ Features
- 📄 Upload **PDF or TXT resumes** (automatic text extraction with PyPDF2).
- 🔎 Find **top job matches** using semantic embeddings (`all-MiniLM-L6-v2`).
- ⚡ **FastAPI backend** with `/match` endpoint for programmatic access.
- 🎨 **Streamlit frontend** for interactive job matching.
- 📊 Easily extend with new jobs and resumes.

---

## 📂 Project Structure
resume-job-match/
├── app/ # FastAPI backend
│ ├── main.py
│ └── matcher.py
├── streamlit_app/ # Streamlit frontend
│ └── ui.py
├── scripts/ # Indexing scripts
│ ├── init.py
│ ├── index_jobs.py
│ └── utils.py
├── data/ # Sample data
│ ├── sample_jobs.json
│ └── sample_resumes/
├── models/ # Saved embeddings
├── requirements.txt
├── README.md
└── Dockerfile


---

## 🚀 Getting Started

### 1️⃣ Clone the repo
---
git clone https://github.com/<your-username>/resume-job-match.git
cd resume-job-match

---
### Setup environment
python -m venv venv
source venv/bin/activate     # For Linux/Mac
venv\Scripts\activate        # For Windows
pip install --upgrade pip
pip install -r requirements.txt

---
### Index Sample Jobs
python -m scripts.index_jobs

---
### Start the Backend
python -m uvicorn app.main:app --reload --port 8000

---
### Start the frontend (On another terminal)
streamlit run streamlit_app/ui.py

```bash
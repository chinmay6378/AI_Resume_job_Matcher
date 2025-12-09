# 🧠 AI Resume Analyzer + Job Matcher

An AI-powered web application that analyzes resumes using a Hugging Face open-source Large Language Model (LLM) and matches candidates to relevant job descriptions using semantic search.

This project is designed to be beginner-friendly while still demonstrating real-world AI/ML concepts used in high-paying roles.

---

## 🚀 Features

✅ Upload resume in PDF format  
✅ Automatically extract text from resume  
✅ Use Hugging Face LLM to extract technical skills  
✅ Match resume skills to real job descriptions  
✅ Display best matching jobs instantly  

---

## 🛠 Tech Stack

Frontend:
- Streamlit

Backend:
- FastAPI

AI / NLP:
- Hugging Face Inference API (`google/flan-t5-base`)
- Lang-chain logic (lightweight usage)
- Sentence Transformers for embeddings

Database:
- ChromaDB (Vector Database)

---

## 📁 Project Structure

ai-resume-job-matcher/
│
├── backend/
│ ├── main.py
│ ├── llm.py
│ ├── resume_parser.py
│ ├── vector_db.py
│ ├── job_matcher.py
│ ├── load_jobs.py
│ ├── requirements.txt
│ └── .env
│
├── frontend/
│ ├── app.py
│ └── requirements.txt
│
├── jobs_dataset/
│ └── jobs.json
│
└── README.md


---

## 🔑 Setting Up Hugging Face API Key

1. Create a free account at:
   https://huggingface.co

2. Generate your Access Token:
   - Go to Profile → Settings → Access Tokens
   - Click **New token**
   - Copy the token

3. Create a `.env` file inside `backend/`:

HUGGINGFACE_API_KEY=your_api_key_here


⚠️ Never upload your `.env` file to GitHub.

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-url>
cd ai-resume-job-matcher


2️⃣ Install Backend Dependencies

cd backend
pip install -r requirements.txt

3️⃣ Install Frontend Dependencies

cd ../frontend
pip install -r requirements.txt

🧩 Load Job Data into Vector Database
cd backend
python load_jobs.py

▶️ Run the Application
Start Backend Server
cd backend
uvicorn main:app --reload


FastAPI will run at:

http://127.0.0.1:8000

Start Frontend (Streamlit)

Open a new terminal:

cd frontend
streamlit run app.py


Your web app will open at:

http://localhost:8501
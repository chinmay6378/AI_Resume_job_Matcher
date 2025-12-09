from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from pypdf import PdfReader

from job_matcher import analyze_and_match

app = FastAPI()

# ✅ Allow Streamlit Cloud or browser to call your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later you can restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    # Read PDF in memory (no disk saving)
    contents = await file.read()
    pdf_file = BytesIO(contents)
    reader = PdfReader(pdf_file)

    resume_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    skills, jobs = analyze_and_match(resume_text)

    return {
        "skills": skills,
        "matched_jobs": jobs
    }
@app.get("/health")
def health():
    return {"status": "ok"}

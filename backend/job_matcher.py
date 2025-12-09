from transformers import pipeline
from vector_db import search_jobs

# Hugging Face model
model = pipeline("text-generation", model="google/flan-t5-base")

def analyze_resume(text):
    prompt = f"Extract skills from this resume:\n{text}"
    output = model(prompt, max_length=200)
    return output[0]["generated_text"]

def match_jobs(skills_text):
    results = search_jobs(skills_text)
    return results

from llm import extract_skills
from vector_db import search_jobs

def analyze_and_match(resume_text):
    skills = extract_skills(resume_text)
    matched_jobs = search_jobs(skills)

    return skills, matched_jobs


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import re

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

llm = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer
)

def clean_text(text: str) -> str:
    text = re.sub(r"http\S+", "", text)           # remove links
    text = re.sub(r"\S+@\S+", "", text)           # remove emails
    text = re.sub(r"\+?\d[\d\s-]{8,}\d", "", text) # remove phone
    return text

def extract_skills(text: str) -> str:
    text = clean_text(text)

    prompt = f"""
Extract only technical and professional skills from this resume.
Do NOT include name, email, phone, or links.
Return comma separated skills only.

Resume:
{text}
"""

    result = llm(prompt, max_new_tokens=150, do_sample=False)
    return result[0]["generated_text"]

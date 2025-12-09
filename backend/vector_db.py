import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Persistent storage location
client = chromadb.PersistentClient(path="./vector_store")

collection = client.get_or_create_collection("jobs")

def add_job(job_id, text):
    embedding = model.encode(text).tolist()
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[str(job_id)]
    )

def search_jobs(query):
    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    if not results or not results.get("documents") or not results["documents"][0]:
        return []

    return results["documents"][0]

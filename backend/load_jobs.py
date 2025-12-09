import json
from vector_db import add_job, collection

# Clear old data
try:
    existing = collection.get()
    if existing["ids"]:
        collection.delete(ids=existing["ids"])
        print("Old jobs cleared")
except:
    pass

# Load new jobs
with open("../jobs_dataset/jobs.json") as f:
    jobs = json.load(f)

# Insert into vector DB
for job in jobs:
    text = f"{job['title']} - {job['description']}"
    add_job(job["id"], text)

print("✅ Jobs stored in vector database successfully")

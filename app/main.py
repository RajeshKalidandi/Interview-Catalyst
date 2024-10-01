from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_job_listings_table, get_job_listings
from app.celery_app import scrape_and_store_jobs

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    create_job_listings_table()

@app.get("/")
async def root():
    return {"message": "Welcome to Interview Catalyst API"}

@app.get("/trigger-job-scraping/")
async def trigger_job_scraping(query: str):
    task = scrape_and_store_jobs.delay(query)
    return {"message": "Job scraping task triggered", "task_id": task.id}

@app.get("/job-listings/")
async def get_all_job_listings():
    return get_job_listings()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

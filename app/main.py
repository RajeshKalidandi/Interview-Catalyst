from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Interview Catalyst API"}

@app.get("/api/jobs")
async def get_jobs():
    # TODO: Implement job fetching logic
    return {"jobs": []}

@app.post("/api/apply")
async def apply_job(job_id: int):
    # TODO: Implement job application logic
    return {"status": "Application submitted", "job_id": job_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import os
from supabase import create_client, Client
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class JobListing(BaseModel):
    title: str
    company: str
    location: str
    link: str

def create_job_listings_table():
    # This function now only needs to be called once to set up the table
    supabase.table("job_listings").create({
        "id": "int8",
        "title": "text",
        "company": "text",
        "location": "text",
        "link": "text",
        "created_at": "timestamptz"
    }, primary_key="id")

def insert_job_listing(job: JobListing):
    return supabase.table("job_listings").insert(job.dict()).execute()

def get_job_listings():
    return supabase.table("job_listings").select("*").execute()

# Keep the existing functions for backward compatibility
def get_jobs():
    return get_job_listings()

def submit_application(job_id: int, user_id: int):
    # TODO: Implement actual application submission to Supabase
    return supabase.table('applications').insert({"job_id": job_id, "user_id": user_id}).execute()

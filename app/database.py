import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_jobs():
    # TODO: Implement actual job fetching from Supabase
    return supabase.table('jobs').select('*').execute()

def submit_application(job_id: int, user_id: int):
    # TODO: Implement actual application submission to Supabase
    return supabase.table('applications').insert({"job_id": job_id, "user_id": user_id}).execute()

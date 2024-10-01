from celery import Celery
from app.job_scraper import scrape_linkedin_jobs
from app.database import insert_job_listing

celery_app = Celery('tasks', broker='redis://localhost:6379')

# Load the Celery config
celery_app.config_from_object('celery_config')

# For Windows, we need to add this to ensure the tasks run properly
celery_app.conf.update(
    worker_pool_restarts=True,
)

@celery_app.task
def scrape_and_store_jobs(query: str):
    jobs = scrape_linkedin_jobs(query)
    for job in jobs:
        insert_job_listing(job)
    return f"Scraped and stored {len(jobs)} job listings"
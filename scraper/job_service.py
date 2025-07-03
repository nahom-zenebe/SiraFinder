# services/job_service.py
from scraper.remoteok_scraper import scrape_remoteok
from database.db import jobs_col

def refresh_jobs():
    jobs = scrape_remoteok()
    for job in jobs:
        jobs_col.update_one({"link": job.link}, {"$set": job.__dict__}, upsert=True)

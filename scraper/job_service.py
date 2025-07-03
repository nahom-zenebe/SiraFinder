from scraper.remoteok_scraper import scrape_remoteok
from scraper.ethiojobs_scraper import scrape_ethiojobs
from scraper.dereja_scraper import scrape_dereja
from scraper.reporter_scraper import scrape_reporter_jobs
from scraper.wellfound_scraper import scrape_wellfound
from database.db import jobs_col

def refresh_jobs():
    all_jobs = []
    scrapers = [
        scrape_remoteok,
        scrape_ethiojobs,
        scrape_dereja,
        scrape_reporter_jobs,
        scrape_wellfound
    ]

    for scraper in scrapers:
        try:
            jobs = scraper()
            all_jobs.extend(jobs)
            print(f"✅ {scraper.__name__} returned {len(jobs)} jobs.")
        except Exception as e:
            print(f"❌ Failed to run {scraper.__name__}: {e}")

    # Store in DB (deduplicated by job.link)
    for job in all_jobs:
        try:
            jobs_col.update_one(
                {"link": job.link},
                {"$set": job.__dict__},
                upsert=True
            )
        except Exception as e:
            print(f"❌ Error saving job {job.title}: {e}")

    print(f"🗃️ Total jobs saved/updated: {len(all_jobs)}")

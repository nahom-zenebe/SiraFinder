# scraper/reporter_scraper.py
from models.job import JobPost
import requests
from bs4 import BeautifulSoup

def scrape_reporter_jobs():
    url = "https://www.reporterjobs.com/jobs"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []

    for card in soup.select(".job-listing")[:10]:
        title = card.select_one("h4 a")
        link = "https://www.reporterjobs.com" + title["href"]
        title_text = title.text.strip()
        company = card.select_one(".company").text.strip() if card.select_one(".company") else "Unknown"
        location = card.select_one(".job-location").text.strip() if card.select_one(".job-location") else "Ethiopia"

        jobs.append(JobPost(
            title=title_text,
            company=company,
            link=link,
            description="ReporterJobs Listing",
            location=location,
            tags=["reporter", "ethiopia"]
        ))
    return jobs

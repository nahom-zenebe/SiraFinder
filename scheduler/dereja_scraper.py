# scraper/dereja_scraper.py
from models.job import JobPost
import requests
from bs4 import BeautifulSoup

def scrape_dereja():
    url = "https://www.dereja.com/job"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []

    for job_card in soup.select(".job-content")[:10]:
        title = job_card.select_one("h4 a")
        link = "https://www.dereja.com" + title["href"]
        title_text = title.text.strip()
        company = job_card.select_one(".company-name").text.strip() if job_card.select_one(".company-name") else "Unknown"
        location = job_card.select_one(".job-location").text.strip() if job_card.select_one(".job-location") else "Ethiopia"

        jobs.append(JobPost(
            title=title_text,
            company=company,
            link=link,
            description="Click to see full job description",
            location=location,
            tags=["dereja", "ethiopia"]
        ))
    return jobs

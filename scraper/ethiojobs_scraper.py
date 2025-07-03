# scraper/ethiojobs_scraper.py
from models.job import JobPost
import requests
from bs4 import BeautifulSoup

def scrape_ethiojobs(pages=1):
    base_url = "https://www.ethiojobs.net/search-results-jobs/"
    jobs = []

    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")

        for card in soup.select(".job-listing-item"):
            title = card.select_one(".job-title a").text.strip()
            link = card.select_one(".job-title a")["href"]
            company = card.select_one(".job-company").text.strip() if card.select_one(".job-company") else "Unknown"
            desc = card.select_one(".job-desc").text.strip() if card.select_one(".job-desc") else ""
            location = card.select_one(".job-location").text.strip() if card.select_one(".job-location") else "Ethiopia"

            jobs.append(JobPost(
                title=title,
                company=company,
                link=link,
                description=desc,
                location=location,
                tags=["ethiopia", "ethiojobs"]
            ))
    return jobs

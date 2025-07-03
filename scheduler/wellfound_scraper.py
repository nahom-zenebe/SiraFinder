from models.job import JobPost
import requests
from bs4 import BeautifulSoup

def scrape_wellfound():
    jobs = []
    url = "https://wellfound.com/jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    for post in soup.select(".styles_component__jobInfo")[:5]:
        title = post.select_one(".styles_component__title")
        company = post.select_one(".styles_component__company")
        link = post.select_one("a")

        if title and link:
            jobs.append(JobPost(
                title=title.text.strip(),
                company=company.text.strip() if company else "Unknown",
                link="https://wellfound.com" + link["href"],
                description=post.get_text(strip=True),
                location="Remote",
                tags=["startup", "tech"]
            ))

    return jobs

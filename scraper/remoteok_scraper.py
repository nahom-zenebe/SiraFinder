from models.job import JobPost
import requests
from bs4 import BeautifulSoup


def scrape_remoteok():
    jobs=[]
    html=requests.get("https://remoteok.com").text
    soup=BeautifulSoup(html,"html.parser")
    for post in soup.select(".job"):
        jobs.append(JobPost(
            title=post["data-title"],
            company=post["data-company"],
            link=post["data-url"],
            description=post.get_text(),
            location="Remote",
            tags=["remote", "tech"]
            source=post[""],
            salary=post[""],
        
        ))
    return jobs

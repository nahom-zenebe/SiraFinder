# scheduler/job_dispatcher.py
from telegram import Bot
from database.db import users_col
from services.job_service import get_top_jobs
from ai.summarizer import summarize_job
import os

def send_daily_alerts():
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    jobs = get_top_jobs(limit=3)
    for user in users_col.find():
        for job in jobs:
            summary = summarize_job(job["description"])
            bot.send_message(
                chat_id=user["telegram_id"],
                text=f"📢 New Job: {job['title']} at {job['company']}\n{summary}\n{job['link']}"
            )

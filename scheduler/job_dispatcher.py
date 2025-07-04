from telegram import Bot
from database.db import users_col, jobs_col
from scraper.job_service import refresh_jobs
from ai.summarizer import summarize_job
import os

def send_daily_alerts():
    print("🚀 Sending daily job alerts...")

    # 1. Refresh latest jobs and store in DB
    refresh_jobs()

    # 2. Fetch recently added jobs (you can sort or filter later)
    jobs = list(jobs_col.find().sort("_id", -1).limit(5))

    if not jobs:
        print("⚠️ No jobs found to send.")
        return

    # 3. Initialize bot
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))

    # 4. Send jobs to all users
    for user in users_col.find():
        user_id = user.get("telegram_id")
        if not user_id:
            continue

        for job in jobs:
            try:
                summary = summarize_job(job.get("description", "")[:2000])
                message = (
                    f"📌 *{job.get('title')}* at *{job.get('company')}*\n\n"
                    f"{summary}\n"
                    f"[Apply Now]({job.get('link')})"
                )
                bot.send_message(
                    chat_id=user_id,
                    text=message,
                    parse_mode="Markdown",
                    disable_web_page_preview=False
                )
            except Exception as e:
                print(f"❌ Failed to send job to user {user_id}: {e}")

    print("✅ Job alerts sent successfully.")

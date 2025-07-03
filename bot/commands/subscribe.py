from services.job_service import refresh_jobs
from ai.summerizer import summarize_job



async def subscribe(update, context):
    telegram_id=update.effective_user.id
    refresh_jobs()

    jobs=jobs_col.find().limit(3)

    for job in jobs:
        summary = summarize_job(job["description"])
        await update.message.reply_text(
            f"📌 *{job['title']}* at *{job['company']}*\n{summary}\n[Apply Now]({job['link']})",
            parse_mode="Markdown"
        )

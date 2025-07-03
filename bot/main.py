# bot/main.py
from telegram.ext import ApplicationBuilder
from bot.dispatcher import register_handlers
import os

def run_bot():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    register_handlers(app)
    app.run_polling()

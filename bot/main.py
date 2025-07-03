# bot/main.py
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from bot.dispatcher import register_handlers

def run_bot():
    # Load environment variables from .env
    load_dotenv()

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise Exception("TELEGRAM_BOT_TOKEN is not set in environment!")

    # Build the bot application
    app = ApplicationBuilder().token(token).build()

    # Register commands and callbacks
    register_handlers(app)

    print("🤖 SiraFinder Bot is running...")
    app.run_polling()

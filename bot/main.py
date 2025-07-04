import os
from dotenv import load_dotenv
load_dotenv()
from telegram.ext import ApplicationBuilder
from bot.dispatcher import register_handlers


def run_bot():


    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise Exception("TELEGRAM_BOT_TOKEN is not set in environment!")

    app = ApplicationBuilder().token(token).build()
    register_handlers(app)

    print("🤖 SiraFinder Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    run_bot()


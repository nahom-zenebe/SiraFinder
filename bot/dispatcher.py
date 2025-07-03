# bot/dispatcher.py
from telegram.ext import CommandHandler
from bot.commands import start, subscribe

def register_handlers(app):
    app.add_handler(CommandHandler("start", start.start))
    app.add_handler(CommandHandler("subscribe", subscribe.subscribe))


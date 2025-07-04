from telegram import Update
from telegram.ext import ContextTypes
from database.crud_user import get_user, save_user
from models.user import User


async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    telegram_id=update.effective_user.id
    if not get_user(telegram_id):
        save_user(User(telegram_id))
    
    await update.message.reply_text("👋 Welcome to SiraFinder! Use /set to configure your preferences.") 
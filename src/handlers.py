from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from src.config import db, settings, where


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if not db.contains(where("chat_id") == chat_id):
        db.insert(
            {
                "chat_id": chat_id,
                "username": update.effective_user.username,
            }
        )
    await update.effective_chat.send_message(
        text=f"Listening to {settings.LISTEN_URL}..."
    )


handlers = [
    CommandHandler(
        "start",
        start,
    )
]

import logging

from requests_html import AsyncHTMLSession
from telegram.ext import CallbackContext

from src.config import settings, db

last_check = None


async def check_for_changes(context: CallbackContext):
    global last_check
    sess = AsyncHTMLSession()
    res = await sess.get(settings.LISTEN_URL)
    await sess.close()
    element = res.html.find(settings.CSS_SELECTOR, first=True).html
    last_check = last_check if last_check else element
    if last_check == element:
        logging.info("No changes")
        return
    last_check = element
    for chat in db.all() * 3:
        await context.bot.send_message(
            chat["chat_id"],
            text=f"{settings.LISTEN_URL} changed !!!\n check it out !!!",
            parse_mode="Markdown",
        )

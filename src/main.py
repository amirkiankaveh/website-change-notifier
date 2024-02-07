from telegram.ext import AIORateLimiter, ApplicationBuilder
import logging

from src.config import settings
from src.jobs import check_for_changes
from src.handlers import handlers


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def main():
    application = (
        ApplicationBuilder()
        .token(token=settings.TELEGRAM_TOKEN)
        .rate_limiter(AIORateLimiter())
        .concurrent_updates(True)
        .pool_timeout(100)
        .read_timeout(100)
        .build()
    )
    application.job_queue.run_repeating(check_for_changes, 5)
    application.add_handlers(handlers)

    application.run_polling()

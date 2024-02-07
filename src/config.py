from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from tinydb import TinyDB, where

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NOTIFIER_")

    # Bot Fatehr telegram token
    TELEGRAM_TOKEN: str = None
    # json database path
    DB_PATH: str = "db.json"
    # url to listen for changes
    LISTEN_URL: str = "https://nakamigos.io/"
    # css selector of the element you wanna check
    CSS_SELECTOR: str = "body"


settings = Settings()

db = TinyDB(settings.DB_PATH)

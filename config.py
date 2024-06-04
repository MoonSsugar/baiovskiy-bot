import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    bot_token: str = os.getenv("BOT_TOKEN")


settings = Settings()

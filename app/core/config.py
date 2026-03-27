from dataclasses import dataclass
from dotenv import load_dotenv
import os


@dataclass(frozen=True)
class Settings:
    database_url: str
    cors_origins: list[str]

load_dotenv()

def get_settings() -> Settings:
    return Settings(
        database_url=os.getenv("DATABASE_URL"),
        cors_origins=os.getenv("CORS_ORIGINS")
    )

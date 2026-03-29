import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    database_url: str
    cors_origins: list[str]


load_dotenv()


def get_settings() -> Settings:
    database_url = os.getenv("DATABASE_URL")
    if database_url is None:
        raise ValueError("DATABASE_URL is not set")

    cors_origins_str = os.getenv("CORS_ORIGINS", "")
    cors_origins = [origin.strip() for origin in cors_origins_str.split(",") if origin]
    return Settings(database_url=database_url, cors_origins=cors_origins)

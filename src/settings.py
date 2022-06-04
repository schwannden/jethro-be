import os
from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    GOOGLE_API_KEY: str

    FIEF_API_DOMAIN: str
    FIEF_API_CLIENT_ID: str
    FIEF_API_CLIENT_SECRET: str
    FIEF_API_KEY: str

    GAE_VERSION: Optional[str] = None

    def is_production(self) -> bool:
        return self.GAE_VERSION is not None

    def redirect_url(self) -> str:
        if self.is_production():
            return "https://jethro.schwannden.com"
        return "http://localhost:8080"


def get_settings() -> Settings:
    return Settings()


settings = get_settings()

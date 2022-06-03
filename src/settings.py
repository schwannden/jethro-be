import os

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

    def is_production(self) -> bool:
        if os.environ.get("GAE_VERSION", None) is None:
            return False
        return True


def get_settings() -> Settings:
    return Settings()


settings = get_settings()

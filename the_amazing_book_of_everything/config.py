from typing import Annotated

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    APP_NAME: Annotated[str, Field(env=["APP_NAME"])] = "the-amazing-book-of-everything"


settings = Settings()

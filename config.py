import os
import logging
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):

    db_user: str
    db_pass: str
    db_host: str
    db_port: str

    class Config:

        environment: str = os.getenv("ENVIRONMENT", ".dev_env")

        env_file = environment


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()

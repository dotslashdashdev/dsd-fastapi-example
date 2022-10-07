import os
from typing import Optional

from pydantic import BaseSettings, Field


class GlobalSettings(BaseSettings):
    """Global settings."""

    # This variable will be loaded from the .env file. However, if there is a
    # shell environment variable having the same name, that will take precedence.

    # the class Field is necessary while defining the global variables
    ENV_STATE: Optional[str] = Field(..., env="ENV_STATE")

    PROJECT_NAME: str = "dsd-fastapi-example"
    API_V1_STR: str = "/example/api/v1"

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"


class LocalSettings(GlobalSettings):
    """Local settings"""


class DevSettings(GlobalSettings):
    """Development settings"""


class ProdSettings(GlobalSettings):
    """Production Settings"""


class FactorySettings:
    """Returns a settings instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "local":
            return LocalSettings()
        elif self.env_state == "dev":
            return DevSettings()
        elif self.env_state == "prod":
            return ProdSettings()

        raise Exception("ENV_STATE 환경변수가 누락 되었습니다")


settings = FactorySettings(os.getenv("ENV_STATE"))()

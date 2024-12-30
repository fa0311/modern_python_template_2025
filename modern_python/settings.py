from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    auth_key: str = Field(validation_alias="auth_key")
    api_key: str = Field(alias="api_key")

    def __init__(self):
        super().__init__()

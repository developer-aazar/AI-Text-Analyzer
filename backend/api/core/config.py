from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    ai_api_key: str 
    ai_model: str = "gemini-3.6-flash"

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Setting()


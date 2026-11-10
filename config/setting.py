
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "Local File Checker"

    scan_directory: list = ["~/Documents", "~/Downloads", "~/Pictures"]

    database_url: str = "sqlite:///./file_checker.db"

    log_level: str = "INFO"

    log_file: str = "file_checker.log"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()

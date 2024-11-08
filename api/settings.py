from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class ApiSettings(BaseSettings):
    base_url: str
    timeout: float = 1.5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="API__",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        extra="ignore",
    )

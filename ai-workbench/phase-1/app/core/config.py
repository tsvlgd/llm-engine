from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "My Mini Workbench"
    model: str ="openai/gpt-oss-120b"
    groq_api_key: str
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()   
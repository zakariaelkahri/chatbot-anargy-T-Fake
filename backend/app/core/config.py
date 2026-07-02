from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "SentinelAI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Database Settings
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/sentinel"

    # LLM Settings
    OLLAMA_BASE_URL: str = "http://ollama:11434"
    OLLAMA_MODEL: str = "mistral-nemo"
    OLLAMA_NUM_CTX: int = 2048
    OLLAMA_NUM_PREDICT: int = 256
    OLLAMA_EMBEDDING_MODEL: str = "nomic-embed-text"
    GEMINI_API_KEY: Optional[str] = None
    GEMINI_MODEL: str = "gemini-1.5-flash"

    # Frappe / ERPNext Settings
    FRAPPE_BASE_URL: str = "http://172.26.144.1:8080"
    FRAPPE_AUTH_TOKEN: Optional[str] = "token 626c7b10b45a3f6:f03cf008ef463a8"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

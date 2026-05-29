from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Ollama Configuration
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
    OLLAMA_CODE_MODEL: str = os.getenv("OLLAMA_CODE_MODEL", "codellama")
    OLLAMA_TIMEOUT: int = int(os.getenv("OLLAMA_TIMEOUT", "120"))
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./vighna_ai.db")
    
    # JWT
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your_super_secret_key")
    JWT_EXPIRATION: int = int(os.getenv("JWT_EXPIRATION", "3600"))
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    
    # CORS
    CORS_ORIGINS: list = [
        "http://localhost:4200",
        "http://localhost:3000",
        "http://localhost:8000"
    ]
    
    class Config:
        case_sensitive = True

settings = Settings()

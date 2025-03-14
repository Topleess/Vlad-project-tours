from pydantic_settings import BaseSettings
from typing import Optional
import secrets


class Settings(BaseSettings):
    # Базовые настройки приложения
    PROJECT_NAME: str = "Туристическое агентство API"
    PROJECT_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Настройки безопасности
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # Время жизни токена - 30 дней
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 43200
    
    # База данных
    DATABASE_URL: str = "sqlite:///./app.db"
    
    class Config:
        env_file = ".env"


settings = Settings() 
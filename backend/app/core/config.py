"""Модуль конфигурации бэкэнда."""
from typing import Optional

from pydantic_settings import BaseSettings
from pydantic import EmailStr


class Settings(BaseSettings):
    """Класс настроек бэкенда."""
    app_title: str = 'Later'
    app_description: str = 'Later'
    #database_url: str
    postgres_db: str = 'postgres'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    postgres_host: str = None # 'localhost'
    postgres_port: str = '5432'
    secret: str = 'A_SECRET_word!'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    # redis_url: Optional[str] = None
    # admin_user_model: Optional[str] = None
    # admin_user_model_username_field: Optional[str] = None
    # admin_secret_key: Optional[str] = None


    class Config:
        """Конфигурация класса настроек."""
        env_file = '.env'


settings = Settings()

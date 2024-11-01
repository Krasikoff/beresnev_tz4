from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_title: str = 'Input title in .env'
    app_title: str = 'Later'
    app_description: str = 'Later'
    postgres_db: str = 'postgres'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    postgres_host: str = 'localhost'
    postgres_port: str = '5432'

    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()

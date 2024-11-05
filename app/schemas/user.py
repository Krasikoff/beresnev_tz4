"""Модуль схем пользователя."""
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Класс схемы для чтения."""
    username: str


class UserCreate(schemas.BaseUserCreate):
    """Класс схемы для создания."""
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    """Класс схемы для обновления."""
    username: str

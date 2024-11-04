"""Модуль модели пользователя."""
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """Класс модели пользователя."""
    username = Column(String, nullable=False)

    def __str__(self):
        return f' #{self.id}  {self.username}'

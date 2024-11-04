"""Модуль схем task."""
from typing import Optional

from pydantic import BaseModel

from app.core.constants import Status


class TaskBase(BaseModel):
    """Класс схемы для чтения."""
    name: str
    descr: str
    status: Optional[Status]

    class Config:
        from_attributes = True


class TaskCreation(BaseModel):
    """Класс схемы для создания."""
    name: str
    descr: str
    status: Optional[Status]


class TaskUpdate(BaseModel):
    """Класс схемы для обновления."""
    name: str
    descr: str
    status: Optional[Status]

"""Модуль модели."""
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType

from app.core.constants import Status
from app.core.db import Base


class Task(Base):
    """Класс модели."""
    name = Column(String(100), nullable=False)
    descr = Column(Text())
    status = Column(
        ChoiceType(Status), default=Status.NO_STATUS, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', backref='task', foreign_keys=[user_id])

    def __str__(self):
        return f'#{self.id} : {self.name} - {self.status}'

    def __repr__(self):
        return (
            f'Задача {self.name} - {self.status}'
        )

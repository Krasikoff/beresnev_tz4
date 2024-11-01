# app/models/meeting_room.py
from sqlalchemy import Column, String, Text
# Импортируйте новую функцию.
from sqlalchemy.orm import relationship

from app.core.db import Base


class MeetingRoom(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    # Установите связь между моделями через функцию relationship.
    reservation = relationship(
        'Reservation', cascade='delete', back_populates='meetingroom')

    def __str__(self):
        return f' #{self.id} {self.name}'

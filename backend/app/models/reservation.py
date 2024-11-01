# app/models/reservation.py
# Импортируйте классы.
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.core.db import Base


class Reservation(Base):
    from_reserve = Column(DateTime)
    to_reserve = Column(DateTime)
    # Столбец с внешним ключом: ссылка на таблицу meetingroom.
    meetingroom_id = Column(Integer, ForeignKey('meetingroom.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='reservation')
    meetingroom = relationship('MeetingRoom', back_populates='reservation')

    def __str__(self):
        return f'#{self.id} : {self.from_reserve} to {self.to_reserve}'

    def __repr__(self):
        return (
            f'Уже забронировано с {self.from_reserve} по {self.to_reserve}'
        )

from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator, root_validator


# FROM_TIME = '2022-04-24T11:00'
FROM_TIME = (datetime.now() + timedelta(minutes=10)).isoformat()
# TO_TIME = '2022-04-24T12:00'
TO_TIME = (datetime.now() + timedelta(hours=1, minutes=10)).isoformat()


# Базовый класс схемы, от которого наследуем все остальные.
class ReservationBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        extra = Extra.forbid


class ReservationUpdate(ReservationBase):

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


# Этот класс наследуем от ReservationUpdate с валидаторами.
class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int
    user_id: Optional[int]

    class Config:
        orm_mode = True

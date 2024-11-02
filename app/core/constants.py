from enum import Enum

STATUS = (
    ('NO STATUS', 'Не начата'),
    ('WORKING ON', 'В работе'),
    ('FINISHED', 'Закончена'),
)


class Status (str, Enum):
    NO_STATUS = 'Не начата'
    WORKING_ON = 'В работе'
    FINISHED = 'Закончена'

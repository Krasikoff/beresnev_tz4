from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy_utils import ChoiceType
from app.core.constants import STATUS
from app.core.db import Base
import datetime


class Task(Base):
    name = Column(String(100), nullable=False)
    descr = Column(Text())
    status = Column(ChoiceType(STATUS), default=STATUS[0][0])
    created_date = Column(
        DateTime, default=datetime.datetime.now(datetime.timezone.utc)
    )

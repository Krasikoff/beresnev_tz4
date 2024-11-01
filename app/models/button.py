from sqlalchemy import Column, String, Text, Boolean, DateTime
from sqlalchemy_utils import ChoiceType
from app.core.constants import STATUS
from app.core.db import Base
import datetime


class Button(Base):
    name = Column(String(100), nullable=False)
    descr = Column(Text())
    status = Column(ChoiceType(STATUS), default=STATUS[0][0])
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

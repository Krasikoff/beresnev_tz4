from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Text

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    username = Column(String, nullable=False)
    def __str__(self):
        return f' #{self.id}  {self.username}'

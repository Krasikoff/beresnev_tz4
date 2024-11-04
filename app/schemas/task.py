from pydantic import BaseModel
from app.core.constants import Status
from typing import Optional


class TaskBase(BaseModel):
    name: str
    descr: str
    status: Optional[Status]

    class Config:
        from_attributes = True


class TaskCreation(BaseModel):
    name: str
    descr: str
    status: Optional[Status]


class TaskUpdate(BaseModel):
    name: str
    descr: str
    status: Optional[Status]

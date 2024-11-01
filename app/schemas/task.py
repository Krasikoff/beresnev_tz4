from datetime import datetime
from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    descr: str
    status: str
    created_date: datetime

    class Config:
        orm_mode = True


class ButtonCreation(BaseModel):
    name: str
    descr: str
    status: str


class ButtonUpdate(BaseModel):
    name: str
    descr: str
    status: str

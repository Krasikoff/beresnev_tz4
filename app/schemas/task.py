from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    descr: str
    status: str

    class Config:
        from_attributes = True


class TaskCreation(BaseModel):
    name: str
    descr: str
    status: str


class TaskUpdate(BaseModel):
    name: str
    descr: str
    status: str

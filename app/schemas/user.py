from fastapi_users import schemas
from typing import Optional


class UserRead(schemas.BaseUser[int]):
    username: str
    # fist_name: Optional[str]
    # last_name: Optional[str]


class UserCreate(schemas.BaseUserCreate):
    username: str
    # fist_name: Optional[str]
    # last_name: Optional[str]


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    # fist_name: Optional[str]
    # last_name: Optional[str]


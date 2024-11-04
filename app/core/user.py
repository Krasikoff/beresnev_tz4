from typing import Optional, Union
from pydantic import BaseModel
from fastapi import Depends, Request, Response
from fastapi.responses import JSONResponse
from fastapi_users.schemas import model_dump
from fastapi_users import (
    BaseUserManager, FastAPIUsers, IntegerIDMixin, InvalidPasswordException
)
from fastapi_users.authentication.strategy import Strategy
from fastapi_users.authentication.transport import Transport
from fastapi_users import models
from fastapi_users.authentication import (
    JWTStrategy,
    AuthenticationBackend,
    BearerTransport,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.redis import (
    get_refresh_token,
    set_refresh_token,
    create_refresh_token,
)
from app.core.config import settings


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


class BearerResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class MyBearerTransport(BearerTransport):
    async def get_login_response(
            self,
            token: str,
            refresh_token: str,
    ) -> Response:
        bearer_response = BearerResponse(
            access_token=token,
            token_type="bearer",
            refresh_token=refresh_token,
        )
        return JSONResponse(model_dump(bearer_response))


bearer_transport = MyBearerTransport(tokenUrl='auth/login')


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret, lifetime_seconds=86400)


class MyTransport(Transport):
    async def get_login_response(
            self, token: str, refresh_token: str) -> Response:
        ...  # pragma: no cover


class MyAuthenticationBackend(AuthenticationBackend):
    name: str
    transport: MyTransport

    async def login(
        self, strategy: Strategy[models.UP, models.ID], user: models.UP
    ) -> Response:
        try:
            refresh_token = await get_refresh_token(user.id)
        except Exception as e:
            print(e)
            refresh_token = await create_refresh_token(
                data={"sub": user.id}
            )
            result = await set_refresh_token(user.id, refresh_token)
            if not result:
                raise Exception
        token = await strategy.write_token(user)
        return await self.transport.get_login_response(token, refresh_token)


auth_backend = MyAuthenticationBackend(
    name='jwt',
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int],):

    async def validate_password(
            self,
            password: str,
            user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 3:
            raise InvalidPasswordException(
                reason='Password should be at least 3 characters'
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason='Password should not contain e-mail'
            )

    async def on_after_register(
            self, user: User, request: Optional[Request] = None
    ):
        print(f'Пользователь {user.email} зарегистрирован.')


async def get_user_manager(
        user_db: SQLAlchemyUserDatabase = Depends(get_user_db)
):
    return UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

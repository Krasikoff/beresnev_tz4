"""Роутеры /users/"""
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.redis import get_refresh_token
from app.core.user import auth_backend, fastapi_users, get_jwt_strategy
from app.crud.user import user_crud
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)


@router.post("/auth/refresh")
async def refresh_token(
    refresh_token: str,
    session: AsyncSession = Depends(get_async_session),
):
    SECRET_KEY = 'SOME_SECRET_KEY'
    ALGORITHM = "HS256"

    strategy = get_jwt_strategy()

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        if user_email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate credentials")
        redis_refresh_token = await get_refresh_token(user_email)
        if redis_refresh_token != refresh_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid refresh token")
        user = await user_crud.get_by_attribute('email', user_email, session)
        """A JWT can't be invalidated: it's valid until it expires.
           await strategy.destroy_token(access_token, user)
           maybe change a secret word."""
        access_token = await strategy.write_token(user)
        return {"access_token": access_token, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials")

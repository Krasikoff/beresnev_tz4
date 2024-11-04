from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users.authentication.strategy import Strategy
from fastapi_users import models
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
import jwt
from jose import JWTError
from app.core.user import (
    auth_backend, 
    fastapi_users,
    get_jwt_strategy,
    current_user,
    MyAuthenticationBackend,
)
from app.core.redis import get_refresh_token, get_keys_by_value
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.models import User
from app.crud.user import user_crud

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
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate credentials")
        redis_refresh_token = await get_refresh_token(user_id)
        if redis_refresh_token != refresh_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid refresh token")
        user = await user_crud.get(user_id, session)
        access_token = await strategy.write_token(user)
        return {"access_token": access_token, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials")

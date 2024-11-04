import aioredis
import pickle
from datetime import datetime, timedelta
from jwt import encode

redis = aioredis.from_url("redis://localhost")


async def get_refresh_token(user_id):
    value = await redis.get(user_id)
    unpickled_refresh_token = pickle.loads(value)
    return unpickled_refresh_token


async def set_refresh_token(user_id, refresh_token):
    pickled_refresh_token = pickle.dumps(refresh_token)
    result = await redis.set(user_id, pickled_refresh_token)
    return result


async def get_keys_by_value(value) -> int | None:
    keys = await redis.keys()
    for key in keys:
        if await redis.get(key) == pickle.dumps(value):
            return int(key)
    return None


async def create_refresh_token(data: dict) -> str:
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    SECRET_KEY = 'SOME_SECRET_KEY'
    ALGORITHM = "HS256"
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

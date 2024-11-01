from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr
from sqlalchemy import Column, Integer
from app.core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

database_url = (
    f'postgresql+asyncpg://{settings.postgres_user}:'
    f'{settings.postgres_password}@{settings.postgres_host}:'
    f'{settings.postgres_port}/{settings.postgres_db}'
)
print(database_url)
engine = create_async_engine(database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session

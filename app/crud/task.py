"""Модуль дополнений к базовому CRUD."""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import Status
from app.crud.base import CRUDBase
from app.models import Task, User


class CRUDTask(CRUDBase):
    """Класс дополнения к базовому CRUD."""
    async def get_multy_with_filter(
            self,
            status: Optional[Status],
            user: Optional[User],
            session: AsyncSession
    ):
        """Все объекты с фильтрами статус и пользователь."""
        db_objs = await session.execute(
            select(Task)
        )
        if status:
            db_objs = await session.execute(
                select(Task).filter(status == status,)
            )
        if user:
            db_objs = await session.execute(
                select(Task).filter(Task.user_id == user.id,)
            )
        if status and user:
            db_objs = await session.execute(
                select(Task).filter(
                    Task.user_id == user.id, Task.status == status,)
            )
        return db_objs.scalars().all()


task_crud = CRUDTask(Task)

"""Модуль с валидаторами."""
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.task import task_crud
from app.models import Task, User


async def check_task_exists(
        task_id: int,
        session: AsyncSession,
) -> Task:
    """Проверка существует ли task."""
    task = await task_crud.get(task_id, session)
    if task is None:
        raise HTTPException(
            status_code=404,
            detail='Нет такого task!'
        )
    return task


async def check_task_owner(
        task: Task,
        user: User,
        session: AsyncSession,
) -> Task:
    """ПРоверка принадлежности пользователю."""
    if task.user_id != user.id and not user.is_superuser:
        raise HTTPException(
            status_code=404,
            detail='Не свой task удалять или изменять нельзя!'
        )
    return task

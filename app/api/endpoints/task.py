from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.core.user import current_user

from app.schemas.task import TaskBase, TaskCreation, TaskUpdate
from app.crud.task import task_crud
from app.models import User
from app.api.validators import check_task_exists, check_task_owner 

router = APIRouter()

@router.post(
    '/',
    response_model=TaskBase,
    response_model_exclude_none=True,
)
async def create_new_task(
        task: TaskCreation,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Только для суперюзеров."""
    new_task = await task_crud.create(task, user, session)
    return new_task

@router.get(
    '/',
    response_model=list[TaskBase],
    response_model_exclude_none=True,
)
async def get_all_tasks(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    "возможностью фильтрации по статусу и принадлежность пользователю. "
    all_tasks = await task_crud.get_multi(session)
    return all_tasks


@router.put(
    '/{task_id}',
    response_model=TaskBase,
    response_model_exclude_none=True,
)
async def partially_update_task(
        task_id: int,
        obj_in: TaskUpdate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Только для суперюзеров."""
    task = await check_task_exists(
        task_id, session
    )
    await check_task_owner(task, user, session)
    # if obj_in.name is not None:
    #     await check_name_duplicate(obj_in.name, session)
    task = await task_crud.update(
        task, obj_in, session
    )
    return task


@router.delete(
    '/{task_id}',
    response_model=TaskBase,
    response_model_exclude_none=True,
)
async def remove_task(
        task_id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Проверка своего"""
    task = await check_task_exists(task_id, session)
    await check_task_owner(task, user, session)
    task = await task_crud.remove(task, session)
    return task

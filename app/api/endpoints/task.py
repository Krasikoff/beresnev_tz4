from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_task_exists, check_task_owner
from app.core.constants import Status
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.task import task_crud
from app.models import User
from app.schemas.task import TaskBase, TaskCreation, TaskUpdate

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
    """Создание нового task."""
    new_task = await task_crud.create(task, session, user)
    return new_task


@router.get(
    '/{status}',
    response_model=list[TaskBase],
    response_model_exclude_none=True,
)
async def get_all_tasks_filter(
        status: Status,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    "C возможностью фильтрации по статусу и принадлежность пользователю. "
    if status:
        print(status)
        all_tasks = await task_crud.get_multy_with_filter(
            status, user, session=session,
        )
    return all_tasks


@router.get(
    '/{status}/superuser/',
    response_model=list[TaskBase],
    response_model_exclude_none=True,
)
async def get_all_tasks_filter(
        status: Status,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session),
):
    "C возможностью фильтрации по статусу режим суперюзер."
    if status:
        if user.is_superuser:
            all_tasks = await task_crud.get_multy_with_filter(
                status, session=session,
            )
    else:
        raise HTTPException(status_code=401,
                            detail="Вы не superuser")
    return all_tasks


@router.get(
    '/',
    response_model=list[TaskBase],
    response_model_exclude_none=True,
)
async def get_all_tasks(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    "Все принадлежащие пользователю task."
    all_tasks = await task_crud.get_multy_with_filter(
        status=None,
        user=user,
        session=session,
    )
    return all_tasks


@router.get(
    '/superuser/',
    response_model=list[TaskBase],
    response_model_exclude_none=True,
)
async def get_all_tasks(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    "Все task не зависимо от принадлежности user."
    if user.is_superuser:
        all_tasks = await task_crud.get_multi(session)
        return all_tasks
    else:
        raise HTTPException(status_code=401,
                            detail="Вы не superuser")


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
    """Обновляет все поля task."""
    task = await check_task_exists(
        task_id, session
    )
    await check_task_owner(task, user, session)
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

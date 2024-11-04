from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.crud.base import CRUDBase
from app.models import Task, User
from app.core.constants import Status


class CRUDTask(CRUDBase):
    async def get_multy_with_filter(
            self,
            status: Status,
            user: User,
            session: AsyncSession
    ):
        db_objs = await session.execute(
            select(Task).filter(
                Task.status == status, Task.user_id == user.id))
        return db_objs.scalars().all()


task_crud = CRUDTask(Task)

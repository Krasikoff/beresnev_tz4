from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.task import Task
from sqlalchemy import update


class CRUDTask(CRUDBase):
#     async def create(
#             self,
#             name: str,
#             is_moscow: bool,
#             text: str,
#             picture: str,
#             file: str,
#             is_department: bool,
#             is_active: bool,
#             session: AsyncSession,
#     ):
#         db_obj = self.model(name=name,
#                             is_moscow=is_moscow,
#                             text=text,
#                             picture=picture,
#                             file=file,
#                             is_department=is_department,
#                             is_active=is_active
#                             )
#         session.add(db_obj)
#         await session.commit()
#         await session.refresh(db_obj)
#         return db_obj
        pass

task_crud = CRUDTask(Task)

# app/main.py
from fastapi import FastAPI
from sqladmin import Admin

# Импортируем главный роутер.
from app.api.routers import main_router
from app.core.config import settings
from app.core.db import engine
from app.admin.view import UserAdmin #ReservationAdmin, MeetingRoomAdmin, FileAdmin
from app.admin.auth import AdminAuth
from app.core.init_db import create_first_superuser



app = FastAPI(title=settings.app_title)
authentication_backend = AdminAuth(secret_key="111")
admin = Admin(
    app=app, engine=engine,
    authentication_backend=authentication_backend
)


admin.add_view(UserAdmin)
#admin.add_view(ReservationAdmin)
#admin.add_view(MeetingRoomAdmin)
#admin.add_view(FileAdmin)

# Подключаем главный роутер.
app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()

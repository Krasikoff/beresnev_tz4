from fastapi import FastAPI
#from fastapi import HTTPException, Request
from starlette.staticfiles import StaticFiles

#from app.api.button import router as button
from app.api.user import router as user
from app.core.config import settings

app = FastAPI(title=settings.app_title)

app.include_router(user)
#app.include_router(button)
#app.include_router(render)

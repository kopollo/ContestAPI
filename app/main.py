import os

from fastapi import FastAPI, Depends
from starlette.staticfiles import StaticFiles

from app.auth import get_current_admin_user
from app.database import engine
from app.models import Base

from app.routes import admin_task, public, login, user, views

Base.metadata.create_all(bind=engine)

app = FastAPI()
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")

app.include_router(
    public.router,
    prefix="/api",
    tags=["public"],
)

app.include_router(
    admin_task.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_current_admin_user)]
)

app.include_router(
    login.router,
    tags=["login"],
)

app.include_router(
    user.router,
    tags=["user"],
)
app.include_router(
    views.router,
    tags=["views"],
)

from fastapi import FastAPI, Depends

from app.auth import get_current_admin_user
from app.database import engine
from app.models import Base

from app.routes import admin_task, public, user, debug

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    public.router,
    tags=["public"],
)

app.include_router(
    admin_task.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_current_admin_user)]
)

app.include_router(
    user.router,
    tags=["user"],
)

app.include_router(
    debug.router,
    tags=["user"],
)

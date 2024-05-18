from typing import Union, Annotated

from fastapi import APIRouter, status, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse

from app import schemas, security
from app.auth import authenticate_user, get_current_user

from datetime import timedelta

from app.config import templates
from app.database import get_db
from app.crud.crud import user_crud, task_crud

from fastapi.templating import Jinja2Templates

# app.mount("/static", StaticFiles(directory="static"), name="static")


router = APIRouter()


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )


@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        request=request, name="register.html"
    )


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="base.html"
    )


@router.get("/admin/tasks", response_class=HTMLResponse)
async def admin_task(request: Request):
    return templates.TemplateResponse(
        request=request, name="create_task.html"
    )


@router.get("/tasks", response_class=HTMLResponse)
async def tasks(
        request: Request,
        db: Session = Depends(get_db)
):
    # Переписать на обращение к endpoint api/tasks, чтобы представить настоящую работу с апи
    d = task_crud.get_all(db)
    return templates.TemplateResponse(
        "tasks.html", {"request": request, "tasks": d}
    )


@router.get("/tasks/{task_id}", response_model=schemas.Task)
async def task(
        request: Request,
        task_id: int,
        db: Session = Depends(get_db),
):
    d = task_crud.get_by_id(db, task_id)
    return templates.TemplateResponse(
        "task.html", {"request": request, "task": d}
    )

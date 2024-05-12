from typing import Union, Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas, security
from app.auth import authenticate_user, get_current_user

from datetime import timedelta

from app.database import get_db
from app.crud.crud import task_crud

router = APIRouter()


@router.get("/tasks/", response_model=list[schemas.Task])
async def get_tasks(
        db: Session = Depends(get_db),

):
    tasks = task_crud.get_all(db)
    return tasks

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


@router.post("/tasks", tags=["admin"], response_model=schemas.Task)
async def create_task(
        task: schemas.Task,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    if not current_user.is_teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not a teacher",
        )
    db_task = task_crud.create(db, task)
    return db_task

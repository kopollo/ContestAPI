from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, security

from app.database import get_db
from app.crud.crud import task_crud

router = APIRouter()


@router.get("/tasks/", response_model=list[schemas.Task])
async def get_tasks(
        db: Session = Depends(get_db),
):
    tasks = task_crud.get_all(db)
    return tasks


@router.get("/tasks/{task_id}", response_model=schemas.Task)
async def get_task(
        task_id: int,
        db: Session = Depends(get_db),
):
    return task_crud.get_by_id(db, task_id)

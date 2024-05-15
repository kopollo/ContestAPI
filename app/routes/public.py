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

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, security
from app.auth import authenticate_user, get_current_user, get_current_admin_user

from app.database import get_db
from app.crud.crud import task_crud
from app.crud import crud

router = APIRouter()


@router.post("/tasks", tags=["admin"], response_model=schemas.Task)
async def create_task(
        task: schemas.Task,
        db: Session = Depends(get_db),
        current_admin_user: schemas.User = Depends(get_current_admin_user),
):
    db_task = task_crud.create(db, task)
    return db_task


@router.post("/tasks/{task_id}/tests", tags=["admin"], response_model=schemas.Test)
async def add_test_to_task(
        task_id: int,
        test: schemas.Test,
        db: Session = Depends(get_db),
        current_admin_user: schemas.User = Depends(get_current_admin_user),
):
    test.task_id = task_id
    task = crud.add_test_to_task(db, test)
    return task


@router.get("/tasks/{task_id}/tests", tags=["admin"], response_model=list[schemas.Test])
async def get_task_tests(
        task_id: int,
        db: Session = Depends(get_db),
        current_admin_user: schemas.User = Depends(get_current_admin_user),
):
    tasks = crud.get_task_tests(db, task_id)
    return tasks

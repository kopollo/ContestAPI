from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, security

from app.database import get_db
from app.crud.crud import task_crud
from app.crud import crud

router = APIRouter()


@router.post("/tasks", response_model=schemas.Task)
async def create_task(
        task: schemas.Task,
        db: Session = Depends(get_db),
):
    db_task = task_crud.create(db, task)
    return db_task


# @router.get("/tasks", response_model=list[schemas.Task])
# async def get_tasks(
#         db: Session = Depends(get_db),
# ):
#     return task_crud.get_all(db)


@router.get("/tasks/{task_id}", response_model=list[schemas.Task])
async def get_task(
        task_id: int,
        db: Session = Depends(get_db),
):
    return task_crud.get_by_id(db, task_id)


@router.put("/tasks/{task_id}", response_model=schemas.Task)
async def upd_task(
        task_id: int,
        task: schemas.Task,
        db: Session = Depends(get_db),
):
    task.id = task_id
    return task_crud.update(db, task)


@router.delete("/tasks/{task_id}", response_model=schemas.Task)
async def delete_task(
        task_id: int,
        db: Session = Depends(get_db),
):
    return task_crud.delete(db, task_id)


@router.post("/tasks/{task_id}/tests", response_model=schemas.Test)
async def add_test_to_task(
        task_id: int,
        test: schemas.Test,
        db: Session = Depends(get_db),
):
    test.task_id = task_id
    task = crud.add_test_to_task(db, test)
    return task


@router.get("/tasks/{task_id}/tests", response_model=list[schemas.Test])
async def get_task_tests(
        task_id: int,
        db: Session = Depends(get_db),
):
    tasks = crud.get_task_tests(db, task_id)
    return tasks

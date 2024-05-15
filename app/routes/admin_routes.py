from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, security
from app.auth import authenticate_user, get_current_user

from app.database import get_db
from app.crud.crud import task_crud
from app.crud import crud

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


@router.post("/tasks/{task_id}/tests", tags=["admin"], response_model=schemas.Test)
async def add_test_to_task(
        task_id: int,
        test: schemas.Test,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    if not current_user.is_teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not a teacher",
        )
    test.task_id = task_id
    task = crud.add_test_to_task(db, test)
    return task


@router.get("/tasks/{task_id}/tests", tags=["admin"], response_model=list[schemas.Test])
async def get_task_tests(
        task_id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user),
):
    if not current_user.is_teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not a teacher",
        )
    tasks = crud.get_task_tests(db, task_id)
    return tasks

@router.post("/course/{course_id}/contests", tags=["admin"], response_model=schemas.Contest)
async def add_contest_to_course(
    course_id: int,
    contest: schemas.Contest,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)):
    if not current_user.is_teacher:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not a teacher")
    m2m_table = schemas.CourseContest
    m2m_table.course_id = course_id
    contest = crud.add_contest(db, contest)
    return contest

@router.get("/course/{course_id}/contests", tags=["admin"], response_model=list[schemas.Contest])
async def get_course_contest(
    course_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    if not current_user.is_teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not a teacher",
        )
    contest = crud.get_course_contest(db, contest)
    return contest

@router.post("/course/{course_id}/contest/{contest_id}/tasks/{tasks_id}", tags=["admin"], response_model=schemas.Task)
async def add_task_to_contest(
    task_id: int,
    contest_id: int,
    task: schemas.Task,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)):
    if not current_user.is_teacher:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not a teacher")
    m2m_table = schemas.ContestTask
    m2m_table.contest_id = contest_id
    m2m_table.task_id = task_id
    task = crud.add_task_to_contest(db, task)
    return task

@router.get("/course/{course_id}/contest/{contest_id}/tasks/{tasks_id}", tags=["admin"], response_model=list[schemas.Task])
async def get_contest_task(
    contest_id: int,
    task_id: int,
    task: schemas.Task,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)):
    if not current_user.is_teacher:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not a teacher")
    tasks = crud.get_contest_task(db, task)
    return task
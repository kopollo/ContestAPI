from datetime import timedelta
from typing import Union, Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

# from app.schemas import User, Task, Contest, Course, Submission
from app import schemas, models, crud, security
from app.auth import authenticate_user, get_current_user

from datetime import datetime, timezone, timedelta

from app.database import get_db

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
async def create_user(
        user: schemas.User,
        db: Session = Depends(get_db)
):
    """Add user to db - example docs"""
    # print(user)
    # print("--------")
    db_user = crud.create_user(db, user)
    # print(db_user)
    return db_user


@router.get("/users/", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    """read users - example docs"""
    db_users = crud.get_users(db)
    return db_users


@router.get("/tasks/", response_model=list[schemas.Task])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks


@router.post("/admin/tasks", tags=["admin"], response_model=schemas.Task)
async def create_task(
        task: schemas.Task,
        db: Session = Depends(get_db),
):
    print(task)
    db_task = crud.create_task(db, task)
    return db_task


@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
) -> security.Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return security.Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=schemas.User)
async def read_users_me(
        current_user: Annotated[schemas.User, Depends(get_current_user)],
):
    return current_user

# @router.put("/admin/tasks/{task_id}", tags=["admin"])
# async def update_task(task_id: int):
#     ...

#
# # ----------
# @router.post("/admin/contests", tags=["admin"])
# async def create_contest(contest: Contest) -> Contest:
#     return contest
#
#
# @router.put("/admin/contests/{contest_id}", tags=["admin"])
# async def update_contest(task_id: int) -> Task:
#     ...
#
#
# # ----------
#
# @router.post("/admin/courses", tags=["admin"])
# async def create_course(course: Course) -> Course:
#     return course
#
#
# @router.put("/admin/courses/{course_id}", tags=["admin"])
# async def update_course(task_id: int) -> Task:
#     ...

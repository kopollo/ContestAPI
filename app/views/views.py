from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

# from app.schemas import User, Task, Contest, Course, Submission
from app import schemas, models, crud
from app.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
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
async def create_task(task: schemas.Task, db: Session = Depends(get_db)):
    print(task)
    db_task = crud.create_task(db, task)
    return db_task

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

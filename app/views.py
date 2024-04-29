from fastapi import APIRouter, status

from app.schemas import User, Task
import app.crud as db

router = APIRouter()


@router.post("/users/")
async def add_user(user: User) -> User:
    """Add user to db - example docs"""
    db_user = db.create_user(user)
    print(db_user)
    return user


@router.get("/users/")
async def get_user() -> list[User]:
    users = db.get_users()
    return users


@router.get("/tasks/")
async def get_tasks() -> list[Task]:
    data = db.get_tasks()
    return data


@router.post("/admin/tasks")
async def create_task(task: Task) -> Task:
    db_task = db.create_task(task)
    print(db_task)
    return task

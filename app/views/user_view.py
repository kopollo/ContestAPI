# from fastapi import APIRouter, status
#
# from app.schemas import User, Task, Contest, Course, Submission
# import app.crud as db
#
# router = APIRouter()
#
#
# @router.post("/users/")
# async def add_user(user: User) -> User:
#     """Add user to db - example docs"""
#     db_user = db.create_user(user)
#     print(db_user)
#     return user
#
#
# @router.get("/tasks/")
# async def get_tasks() -> list[Task]:
#     tasks = db.get_tasks()
#     return tasks
#
# @router.get("/users/")
# async def get_user() -> list[User]:
#     users = db.get_users()
#     return users
#

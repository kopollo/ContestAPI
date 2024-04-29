from fastapi import APIRouter, status

from app.schemas import User, Task, Contest, Course, Submission
import app.crud as db

router = APIRouter()


@router.post("/admin/tasks", tags=["admin"])
async def create_task(task: Task) -> Task:
    return task


@router.put("/admin/tasks/{task_id}", tags=["admin"])
async def update_task(task_id: int) -> Task:
    ...


# ----------
@router.post("/admin/contests", tags=["admin"])
async def create_contest(contest: Contest) -> Contest:
    return contest


@router.put("/admin/contests/{contest_id}", tags=["admin"])
async def update_contest(task_id: int) -> Task:
    ...


# ----------

@router.post("/admin/courses", tags=["admin"])
async def create_course(course: Course) -> Course:
    return course


@router.put("/admin/courses/{course_id}", tags=["admin"])
async def update_course(task_id: int) -> Task:
    ...

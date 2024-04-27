from fastapi import APIRouter, status

from app.schemas import User


router = APIRouter()


@router.post("/users/")
async def add_user(user: User):

    return user


@router.get("/users/")
async def add_user(user: User):
    return user

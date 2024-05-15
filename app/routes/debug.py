from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, security

from app.database import get_db
from app.crud.crud import user_crud

router = APIRouter()


@router.get("/users/", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    """read users - example docs"""
    db_users = user_crud.get_all(db)
    return db_users


@router.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """read users - example docs"""
    db_user = user_crud.get_by_id(db, user_id)
    return db_user

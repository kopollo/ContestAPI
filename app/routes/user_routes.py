from typing import Union, Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas, security
from app.auth import authenticate_user, get_current_user

from datetime import timedelta

from app.database import get_db
from app.crud.crud import user_crud

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
async def create_user(
        user: schemas.User,
        db: Session = Depends(get_db)
):
    """Add user to db - example docs"""
    # print(user)
    # print("--------")
    db_user = user_crud.create(db, user)
    # print(db_user)
    return db_user


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


@router.post("/login")
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
        current_user: schemas.User = Depends(get_current_user),
):
    return current_user

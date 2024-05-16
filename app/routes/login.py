from typing import Union, Annotated

from fastapi import APIRouter, status, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse

from app import schemas, security
from app.auth import authenticate_user, get_current_user

from datetime import timedelta

from app.config import templates
from app.database import get_db
from app.crud.crud import user_crud

router = APIRouter()


@router.post("/register/", response_model=schemas.User)
async def create_user(
        user: schemas.User,
        db: Session = Depends(get_db)
):
    """Add user to db - example docs"""
    db_user = user_crud.create(db, user)
    return db_user


@router.post("/login", response_class=RedirectResponse)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    resp = RedirectResponse(url="/me", status_code=303)
    resp.set_cookie("user", user.email)
    return resp


@router.get("/me", response_model=schemas.User)
async def read_users_me(
        current_user: schemas.User = Depends(get_current_user),
):
    return current_user

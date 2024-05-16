from typing import Union, Annotated, Optional

from fastapi import APIRouter, status, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

# from app.schemas import User, Task, Contest, Course, Submission
from app import schemas, models, crud, security
from app.crud.crud import user_crud
from app.database import get_db
from datetime import datetime, timezone, timedelta

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def auth_by_cookie(request: Request) -> Optional[str]:
    try:
        user = request.cookies.get("user")
        return user
    except:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )


def authenticate_user(email: str, password: str, db: Session):
    user = user_crud.get_by_email(db, email)
    if not user:
        return False
    if not password == user.password:
        # НЕ ЗАББЫТЬ ПОМЕНЯТЬ НА ХЕШИ
        return False
    return user


async def get_current_user(
        email: Annotated[str, Depends(auth_by_cookie)],
        db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = user_crud.get_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_admin_user(
        current_user: schemas.User = Depends(get_current_user),
):
    if not current_user.is_teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not a teacher",
        )
    return current_user

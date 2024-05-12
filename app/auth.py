from typing import Union, Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

# from app.schemas import User, Task, Contest, Course, Submission
from app import schemas, models, crud, security
from app.crud.crud import user_crud
from app.database import get_db
from datetime import datetime, timezone, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def authenticate_user(email: str, password: str, db: Session):
    user = user_crud.get_by_email(db, email)
    if not user:
        return False
    if not password == user.password:
        # НЕ ЗАББЫТЬ ПОМЕНЯТЬ НА ХЕШИ
        return False
    return user


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = security.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = user_crud.get_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

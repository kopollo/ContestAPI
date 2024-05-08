from datetime import datetime, timezone, timedelta
from typing import Union, Annotated

from docutils.nodes import status
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.utils import get_db
from app import schemas, models, crud


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


# def get_user(email: str, db: Session = get_db()):
#     user = crud.get_user_by_email(db, email)
#     if user is not None:
#         return user


def authenticate_user(email: str, password: str, db: Session):
    user = crud.get_user_by_email(db, email)
    if not user:
        return False
    if not password == user.password:
        # НЕ ЗАББЫТЬ ПОМЕНЯТЬ НА ХЕШИ
        return False
    return user

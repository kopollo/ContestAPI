from datetime import timedelta
from typing import Union, Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

# from app.schemas import User, Task, Contest, Course, Submission
from app import schemas, models, crud
from app.security import Token, authenticate_user, TokenData
from app.utils import get_db
from datetime import datetime, timezone, timedelta

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(get_db(), email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    """Add user to db - example docs"""
    # print(user)
    # print("--------")
    db_user = crud.create_user(db, user)
    # print(db_user)
    return db_user


@router.get("/users/", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    """read users - example docs"""
    db_users = crud.get_users(db)
    return db_users


@router.get("/tasks/", response_model=list[schemas.Task])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks


@router.post("/admin/tasks", tags=["admin"], response_model=schemas.Task)
async def create_task(task: schemas.Task, db: Session = Depends(get_db)):
    print(task)
    db_task = crud.create_task(db, task)
    return db_task


@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=schemas.User)
async def read_users_me(
        current_user: Annotated[schemas.User, Depends(get_db)],
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
        current_user: Annotated[schemas.User, Depends(get_db)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]

# @router.put("/admin/tasks/{task_id}", tags=["admin"])
# async def update_task(task_id: int):
#     ...

#
# # ----------
# @router.post("/admin/contests", tags=["admin"])
# async def create_contest(contest: Contest) -> Contest:
#     return contest
#
#
# @router.put("/admin/contests/{contest_id}", tags=["admin"])
# async def update_contest(task_id: int) -> Task:
#     ...
#
#
# # ----------
#
# @router.post("/admin/courses", tags=["admin"])
# async def create_course(course: Course) -> Course:
#     return course
#
#
# @router.put("/admin/courses/{course_id}", tags=["admin"])
# async def update_course(task_id: int) -> Task:
#     ...

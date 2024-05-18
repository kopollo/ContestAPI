from fastapi import APIRouter, status, Depends, HTTPException, Form
from sqlalchemy.orm import Session

from app import schemas, security
from app.auth import get_current_user

from app.database import get_db
from app.crud.crud import user_crud, submission_crud
from starlette.responses import RedirectResponse

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


@router.delete("/users/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """read users - example docs"""
    return user_crud.delete(db, user_id)


@router.put("/users/{user_id}", response_model=schemas.User)
async def upd_user(
        user_id: int,
        user: schemas.User,
        db: Session = Depends(get_db),
):
    """read users - example docs"""
    user.id = user_id
    return user_crud.update(db, user)


@router.get("/me", response_model=schemas.User)
async def read_users_me(
        current_user: schemas.User = Depends(get_current_user),
):
    return current_user


@router.get("/submissions", response_model=schemas.Submission)
async def get_user_submissions(
        current_user: schemas.User = Depends(get_current_user),
):

    # crud for subs
    return current_user


@router.get("/submissions", response_model=schemas.Submission)
async def get_user_submissions(
        current_user: schemas.User = Depends(get_current_user),
):
    # crud for subs
    return current_user


@router.post("/tasks/{task_id}")
async def submit(
        task_id: int,
        code: str = Form(),
        # current_user: schemas.User = Depends(get_current_user),
        # db: Session = Depends(get_db)
):

    print(code)
    submission = schemas.Submission(
        user_id=1,
        task_id=task_id,
        code=code,
        status=False,
    )
    # submission_crud.create(db, submission)
    # crud for subs
    return RedirectResponse(f"/tasks/{task_id}", status_code=status.HTTP_303_SEE_OTHER)

from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from app import models, schemas
from app.crud.user_crud import CRUDUser
from app.crud.task_crud import CRUDTask
from app.crud import crud_base

# user_crud = CRUDUser()
task_crud = crud_base.CrudBase(models.Task)
user_crud = crud_base.CrudBase(models.User)
submission_crud = crud_base.CrudBase(models.Submission)
# task_crud = CRUDTask()


def add_test_to_task(db: Session, test: schemas.Test) -> models.Test:
    data = models.Test(**test.model_dump())
    db.add(data)
    db.commit()
    return data


def get_task_tests(db: Session, task_id: int) -> models.Test:
    data = db.query(models.Test).filter(models.Test.task_id == task_id).all()
    return data


def get_user_submissions(db: Session, user_id: int):
    data = db.query(models.Submission).filter(models.Submission.user_id == user_id).all()
    return data



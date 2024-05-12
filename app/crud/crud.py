from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from app import models, schemas
from app.crud.user_crud import CRUDUser
from app.crud.task_crud import CRUDTask

user_crud = CRUDUser()
task_crud = CRUDTask()


def add_test_to_task(db: Session, test: schemas.Test) -> models.Test:
    data = models.Test(**test.model_dump())
    db.add(data)
    db.commit()
    return data


def get_task_tests(db: Session, task_id: int) -> models.Test:
    data = db.query(models.Test).filter(models.Test.task_id == task_id).all()
    return data



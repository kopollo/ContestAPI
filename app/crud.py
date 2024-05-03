from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from . import models, schemas


def get_users(db: Session):
    return db.query(models.User).all()


def get_tasks(db: Session):
    return db.query(models.Task).all()


def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    return db_task


def create_user(db: Session, user: schemas.User):
    # mock_user = User(
    #     email="cat@mail.ru",
    #     password="321",
    #     first_name="andrey",
    #     last_name="best",
    #     is_teacher=True,
    #     group="231-231"
    # )
    db_user = models.Task(**user.model_dump())
    db.add(db_user)
    db.commit()
    return db_user

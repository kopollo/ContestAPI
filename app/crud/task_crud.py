from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from app import models, schemas


class CRUDTask:
    def get_all(self, db: Session):
        return db.query(models.Task).all()

    def get_by_id(self, db: Session, id: int):
        return db.query(models.Task).filter(models.Task.id == id).first()

    def create(self, db: Session, task: schemas.Task) -> models.Task:
        db_task = models.Task(**task.model_dump())
        db.add(db_task)
        db.commit()
        return db_task

    def update(self, db: Session, user: schemas.User) -> models.User:
        db_user = models.User(**user.model_dump())
        db.merge(db_user)
        db.commit()
        return db_user

    def delete(self, db: Session, id: int):
        db_user = self.get_by_id(db, id)
        db.delete(db_user)
        db.commit()
        return db_user

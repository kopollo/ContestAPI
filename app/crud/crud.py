from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from app import models, schemas


class CRUDUser:
    def get_all(self, db: Session):
        return db.query(models.User).all()

    def get_by_mail(self, db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def get_by_id(self, db: Session, id: int):
        return db.query(models.User).filter(models.User.id == id).first()



def get_tasks(db: Session):
    return db.query(models.Task).all()


def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    return db_task




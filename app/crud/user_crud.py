from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from app import models, schemas


class CRUDUser:
    def get_all(self, db: Session):
        return db.query(models.User).all()

    def get_by_mail(self, db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def get_by_id(self, db: Session, id: int):
        return db.query(models.User).get(id)

    def create(self, db: Session, user: schemas.User) -> models.User:
        db_user = models.User(**user.model_dump())
        db.add(db_user)
        db.commit()
        return db_user

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

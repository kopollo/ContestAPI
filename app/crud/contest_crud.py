from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app import models, schemas


class CRUDContest:
    def get_all(self, db: Session):
        return db.query(models.Contest).all()

    def get_by_id(self, db: Session, id: int):
        return db.query(models.Contest).filter(models.Contest.id == id).first()

    def create(self, db: Session, contest: schemas.Contest) -> models.Contest:
        db_contest = models.Contest(**contest.model_dump())
        db.add(db_contest)
        db.commit()
        return db_contest

    def update(self, db: Session, user: schemas.Contest) -> models.Contest:
        db_user = models.Contest(**user.model_dump())
        db.merge(db_user)
        db.commit()
        return db_user

    def delete(self, db: Session, id: int):
        db_user = self.get_by_id(db, id)
        db.delete(db_user)
        db.commit()
        return db_user

from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import Base


class CrudBase:
    def __init__(self, model: Base):
        self.model = model

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def get_by_id(self, db: Session, id: int):
        # Всё сломается, если в таблице нет ID
        return db.query(self.model).filter(self.model.id == id).first()

    def create(self, db: Session, schema: BaseModel):
        res = self.model(**schema.model_dump())
        db.add(res)
        db.commit()
        return res

    def update(self, db: Session, new_model: BaseModel):
        res = models.User(**new_model.model_dump())
        db.merge(res)
        db.commit()
        return res

    def delete(self, db: Session, id: int):
        res = self.get_by_id(db, id)
        db.delete(res)
        db.commit()
        return res

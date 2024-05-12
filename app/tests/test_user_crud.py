from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

from app.crud.crud import user_crud

from app.config import settings
from app import schemas
from app.database import Base

engine = create_engine(settings.db_url_test)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)

user = schemas.User.model_validate({
    "email": "batman@ya.ru",
    "password": "A very nice Item",
    "first_name": "Bat",
    "last_name": "bobic",
    "is_teacher": False,
    "group": "23-123",
    "description": "bad boy",
    "phone": "8 999 988 23 42"
})


def test_add_user():
    with SessionLocal() as s:
        r = user_crud.create(s, user)
        print(r)


def test_get_user():
    with SessionLocal() as s:
        r = user_crud.get_by_id(s, 1)
        print(r)


def test_get_user_by_wrong_email():
    with SessionLocal() as s:
        r = user_crud.get_by_mail(s, "batmdan@ya.ru")
        assert r is None


def test_get_user_by_email():
    with SessionLocal() as s:
        r = user_crud.get_by_mail(s, "batman@ya.ru")
        assert r is not None

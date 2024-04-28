from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
import app.schemas as schemas


def get_users():
    # with get_db() as session:
    #     # session.
    #     ...
    with SessionLocal() as session:
        users = session.query(User).all()
    return users


def create_user(user: schemas.User) -> User:
    mock_user = User(
        email="cat@mail.ru",
        password="321",
        first_name="andrey",
        last_name="best",
        is_teacher=True,
        group="231-231"
    )

    with SessionLocal() as session:
        db_user = User(
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            is_teacher=user.is_teacher,
            group=user.group,
        )
        session.add(db_user)
        session.commit()
    return db_user

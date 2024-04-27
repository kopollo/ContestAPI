from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    is_teacher = Column(Boolean)
    group = Column(String)


class Contest(Base):
    __tablename__ = "contests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))
    # По идее это поле не нужно, т.к я буду писать мапперы, чтобы спрятать БД и доступ к эти полям бессмысленен?
    creator = relationship("User")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    condition = Column(Text)
    input = Column(String)
    output = Column(String)

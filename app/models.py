from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, LargeBinary
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
    photo = Column(LargeBinary)
    description = Column(String)
    phone = Column(Integer)


class Contest(Base):
    __tablename__ = "contests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))
    # По идее это поле не нужно, т.к я буду писать мапперы, чтобы спрятать БД и доступ к эти полям бессмысленен?
    # creator = relationship("User")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    condition = Column(Text)
    input = Column(String)
    output = Column(String)
    note = Column(String, default="")
    max_score = Column(Integer)
    time_limit = Column(Integer)
    memory_limit = Column(Integer)
    tags = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))


class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    creator_id = Column(Integer, ForeignKey("users.id"))


class ProgrammingLanguage(Base):
    __tablename__ = "programmingLanguage"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    version = Column(String)


class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    input = Column(Text)
    output = Column(Text)


class ContestTask(Base):
    __tablename__ = "contestTask"
    # contest_id = Column(Integer)                   fkey
    # task_id = Column(Integer)                      fkey
    # creator_id = Column(Integer)                   fkey


class CourseContest(Base):
    __tablename__ = "courseContest"
    # course_id = Column(Integer)                    fkey
    # theme_id = Column(Integer)                     fkey


class UserCourse(Base):
    __tablename__ = "userCourse"
    # student_id = Column(Integer)                   fkey
    # course_id = Column(Integer)                    fkey


class SubmissionTest(Base):
    __tablename__ = "submissionTest"
    # test_id = Column(Integer)                      fkey
    # submission_id = Column(Integer)                fkey
    score = Column(Integer)


class Submission(Base):
    __tablename__ = "submission"
    id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer)                      fkey
    # task_id = Column(Integer)                      fkey
    # programmingLanguage_id = Column(Integer)       fkey
    # contest_id = Column(Integer)                   fkey
    date = Column(DateTime(), defalut=DateTime.now)
    status = Column(Boolean)
    time = Column(Integer)
    code = Column(Text)
    memory = Column(Integer)
    output = Column(Text)

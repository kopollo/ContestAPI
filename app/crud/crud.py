from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from app import models, schemas
from app.crud.user_crud import CRUDUser
from app.crud.task_crud import CRUDTask

user_crud = CRUDUser()
task_crud = CRUDTask()




from typing import Optional, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    is_teacher: bool
    group: str


class Contest(BaseModel):
    id: int
    name: str
    description: str
    creator: Union[User, None]
    difficulty: int

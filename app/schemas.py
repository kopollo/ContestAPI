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

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "batman@ya.ru",
                    "password": "A very nice Item",
                    "first_name": "Bat",
                    "last_name": "bobic",
                    "is_teacher": False,
                    "group": "23-123",
                }
            ]
        }
    }


class Contest(BaseModel):
    id: int
    name: str
    description: str
    creator: Union[User, None]
    difficulty: int

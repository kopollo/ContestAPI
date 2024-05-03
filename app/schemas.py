from typing import Optional, Union
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: Union[int, None] = None
    email: str
    password: str
    first_name: str
    last_name: str
    is_teacher: bool
    group: str
    description: str
    phone: str

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "email": "batman@ya.ru",
                    "password": "A very nice Item",
                    "first_name": "Bat",
                    "last_name": "bobic",
                    "is_teacher": False,
                    "group": "23-123",
                    "description": "bad boy",
                    "phone": "8 999 988 23 42"
                }
            ]
        }
    }

    # class Config:
    #     orm_mode = True


class Contest(BaseModel):
    id: int
    name: str
    description: str
    creator: Union[User, None] = None
    difficulty: int

    # class Config:
    #     orm_mode = True

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Sample Contest",
                    "description": "This is a sample contest",
                    "creator": {
                        "id": 123,
                        "username": "sample_user"
                    },
                    "difficulty": 3
                }
            ]
        }
    }


class Task(BaseModel):
    id: int
    name: str
    condition: str
    input: str
    output: str
    note: str
    max_score: int
    time_limit: int
    memory_limit: int
    tags: str
    creator_id: Union[User, None] = None

    # class Config:
    #     orm_mode = True

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Cat battle",
                    "condition":
                        """
В компании X есть своя система контроля версий. Эта VCS не умеет анализировать изменения в файлах и может смёржить два реквеста автоматически, если они не содержат изменений в одних и тех же файлах.
В определённый момент запускается робот, который автоматически мёржит в мастер пулл-реквесты. Задача робота — смёржить наибольшее количество изменений, после чего дежурный разработчик собирает текущий мастер в релиз и отдаёт его в тестирование.
Робот принимает на вход список реквестов, отсортированных по времени создания. В данных о каждом реквесте содержится список файлов, которые в нём изменились, и время создания реквеста. В каждом реквесте может быть изменён хотя бы один файл.
Робот должен вернуть массив с идентификаторами реквестов в том порядке, в котором их нужно смёржить. При этом робот должен влить максимум изменений (количество изменённых файлов) без конфликтов в порядке времени создания реквестов.
Напишите код этого робота.
                    """,
                    "input": "На вход подаётся массив реквестов. Длина массива - не более 1000, количество конфликтующих между собой пулл-реквестов заранее не известно.",
                    "output":
                        """
                        Код робота должен экспортироваться в виде CommonJS-модуля вида:
/**
 * @param {PullRequest[]} pullRequests массив PR, отсортированных по времени создания
 * @returns {string[]} идентификаторы реквестов в порядке мёржа
 */
module.exports = function (pullRequests) {
    // ваш код
}""",
                    "note": "Ваше решение не должно использовать внешних зависимостей.",
                    "max_score": 1,
                    "time_limit": 1000,
                    "memory_limit": 1024,
                    "tags": "algorithms, LNP"
                            ""
                }
            ]
        }
    }


# class Course(BaseModel):
#     id: int
#     name: str
#     description: str
#     creator_id: int
#
#     class Config:
#         orm_mode = True
#
#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "id": 1,
#                     "name": "Sample Course",
#                     "description": "This is a sample course",
#                     "creator_id": 123
#                 }
#             ]
#         }
#     }


class userCourse(BaseModel):
    student_id: int
    course_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "student_id": 123,
                    "course_id": 456
                }
            ]
        }
    }


class Submission(BaseModel):
    id: int
    user_id: int
    task_id: int
    programming_language_id: int
    contest_id: int
    date: datetime
    status: bool
    time: int
    code: str
    memory: int
    output: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "user_id": 123,
                    "task_id": 456,
                    "programming_language_id": 789,
                    "contest_id": 101,
                    "date": "2024-04-29T12:00:00",
                    "status": True,
                    "time": 30,
                    "code": "print('Hello, World!')",
                    "memory": 1024,
                    "output": "Hello, World!\n"
                }
            ]
        }
    }


class ProgrammingLanguage(BaseModel):
    id: int
    name: str
    version: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Python",
                    "version": "3.9.2"
                }
            ]
        }
    }


class SubmissionTest(BaseModel):
    test_id: int
    submission_id: int
    score: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "test_id": 1,
                    "submission_id": 123,
                    "score": 80
                }
            ]
        }
    }


class Test(BaseModel):
    id: int
    task_id: int
    input: str
    output: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "task_id": 123,
                    "input": "input_data",
                    "output": "expected_output"
                }
            ]
        }
    }


class ContestTask(BaseModel):
    contest_id: int
    task_id: int
    creator_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "contest_id": 1,
                    "task_id": 123,
                    "creator_id": 456
                }
            ]
        }
    }


class CourseContest(BaseModel):
    course_id: int
    theme_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": 1,
                    "theme_id": 123
                }
            ]
        }
    }

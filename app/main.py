from fastapi import FastAPI

from app.database import engine
from app.models import Base

from app.routes import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)
#
#
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

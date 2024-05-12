from fastapi import FastAPI

from app.database import engine
from app.models import Base

from app.routes import user_routes, admin_routes, generic_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(admin_routes.router, prefix="/admin")
app.include_router(generic_routes.router)

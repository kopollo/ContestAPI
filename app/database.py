from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(settings.db_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

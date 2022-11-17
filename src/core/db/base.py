from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@localhost:3306/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

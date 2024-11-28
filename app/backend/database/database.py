from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind= engine)

Base = declarative_base()

def get_db():
    pass
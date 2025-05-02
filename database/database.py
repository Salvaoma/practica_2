from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalogo import Base

DATABASE_URL = "sqlite:///catalogo.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def crear_base():
    Base.metadata.create_all(bind=engine)

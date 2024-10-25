# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cria o engine do banco SQLite
DATABASE_URL = "sqlite:///finance.db"
engine = create_engine(DATABASE_URL)

# Configura o ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função para criar o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

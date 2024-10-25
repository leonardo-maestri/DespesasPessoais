# models.py
from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Receita(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    valor = Column(Float)
    categoria = Column(String)
    data = Column(Date)

class Despesa(Base):
    __tablename__ = 'despesas'
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    valor = Column(Float)
    categoria = Column(String)
    data = Column(Date)

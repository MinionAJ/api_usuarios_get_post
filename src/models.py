from sqlalchemy import Column, Integer, String
from src.database import Base

class Usuario(Base):
    __tablename__="usuarios"

    id = Column(Integer, primary_key = True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)

from database import Base
from sqlalchemy import Column, Integer, String

class Pet(Base):
    __tablename__= "pet"
    id = Column(Integer, primary_key=True, index=True)
    nome_pet = Column(String)
    especie = Column(String)
    raca = Column(String)
    bloco = Column(String)
    apartamento = Column(String)
    nome_tutor = Column(String)
    telefone_tutor = Column(String)

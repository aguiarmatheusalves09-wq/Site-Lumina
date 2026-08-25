#Aqui é onde vamos gerenciar o banco de dados
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

class Usuarios(Base):
    __tablename__ = "usuarios"
    email = Column(String(100), nullable=False, primary_key=True)
    senha = Column(String(100), nullable=False)
    nome = Column(String(100), nullable=False)
    data_nasc = Column(String(100), nullable=False)
    nickname = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Usuario(email='{self.email}', senha='{self.senha}', nome='{self.nome}', data_nasc='{self.data_nasc}', nickname='{self.nickname}')>"





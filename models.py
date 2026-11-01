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
    nickname = Column(String(100), nullable=False, unique=True)
    sequenciaDiaria = Column(Integer, nullable=False, default=0)
    melhorSequencia = Column(Integer, nullable=False, default=0)
    totalDiasAcesso = Column(Integer, nullable=False, default=0)
    ultimoAcesso = Column(String(100), nullable=True)
    diasSemana = Column(String(200), default="")
    fotoPerfil = Column(String(200), nullable=True, default="")

    def __repr__(self):
        return f"<Usuario(email='{self.email}', senha='{self.senha}', nome='{self.nome}', nickname='{self.nickname}', sequenciaDiaria='{self.sequenciaDiaria}', melhorSequencia='{self.melhorSequencia}', totalDiasAcesso='{self.totalDiasAcesso}', ultimoAcesso='{self.ultimoAcesso}', diasSemana='{self.diasSemana}', fotoPerfil='{self.fotoPerfil}')>"





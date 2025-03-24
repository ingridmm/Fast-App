from sqlalchemy import Column, Integer, String
from database import Base

# Modelo do usuário no banco
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    data_nascimento = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando o banco de dados SQLite
DATABASE_URL = "sqlite:///./users.db"
# Criando conexão com o BD
engine = create_engine(
    # String de conexão com o BD
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criando a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Classe para realizar a criação das classes de modelo do  BD
Base = declarative_base()

# Modelo do usuário no banco
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    data_nascimento = Column(String, nullable=False)

# Criar as tabelas no banco
Base.metadata.create_all(bind=engine)

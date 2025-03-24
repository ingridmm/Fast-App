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
# Classe para realizar a criação das classes de modelo do banco de dados
Base = declarative_base()

# Criar as tabelas no banco
Base.metadata.create_all(bind=engine)

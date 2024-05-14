from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Criação de uma engine para o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criação de uma classe base para a definição de modelos
Base = declarative_base()

# Criação de uma fábrica de sessões para interação com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Função utilitária para obter uma sessão de banco de dados.

    Retorna:
        Uma sessão de banco de dados.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

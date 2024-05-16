from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a URL de conexão com o banco de dados PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Cria o motor do banco de dados, conectando-o ao banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Define a sessão do banco de dados, responsável por executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos do SQLAlchemy
Base = declarative_base()


# Função para obter uma sessão do banco de dados
def get_db():
    """
    Retorna uma sessão do banco de dados.

    Yields:
        Session: Uma sessão do banco de dados.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

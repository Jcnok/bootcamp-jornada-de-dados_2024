from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///database/pokemon.db"

# Cria o engine para o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma sessão local para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a base declarativa para definir os modelos de dados
Base = declarative_base()

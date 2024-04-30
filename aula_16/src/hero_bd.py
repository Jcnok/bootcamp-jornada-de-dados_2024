import os
from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    """
    Modelo para representar um herói.

    Atributos:
        id (int, optional): O ID único do herói.
        name (str): O nome do herói.
        secret_name (str): O nome secreto do herói.
        age (int, optional): A idade do herói.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# Obtém o diretório atual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para a pasta 'database/'
database_directory = os.path.join(current_directory, "..", "database")

# Garante que o diretório exista, caso contrário, cria-o
os.makedirs(database_directory, exist_ok=True)

# Define o caminho completo para o banco de dados
database_path = os.path.join(database_directory, "database.db")

# Cria um mecanismo de banco de dados SQLite no caminho especificado
engine = create_engine(f"sqlite:///{database_path}", echo=True)

# Cria as tabelas no banco de dados
SQLModel.metadata.create_all(engine)

# Cria instâncias de heróis
hero_1 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

# Inicia uma sessão com o banco de dados
with Session(engine) as session:
    # Adiciona os heróis à sessão
    session.add(hero_1)
    session.add(hero_2)
    # Commit das alterações
    session.commit()

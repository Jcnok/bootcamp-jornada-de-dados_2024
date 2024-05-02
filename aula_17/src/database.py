from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
    """
    Função para criar uma sessão do banco de dados.

    Retorna:
        Session: Objeto de sessão para interagir com o banco de dados.
    """
    engine = create_engine("sqlite:///database/projeto.db", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

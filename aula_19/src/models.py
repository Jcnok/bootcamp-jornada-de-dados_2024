from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

# Criação de uma classe base para a definição de modelos
Base = declarative_base()


class Item(Base):
    """
    Modelo para a tabela 'items'.

    Atributos:
        id (int): Identificador único do item (chave primária).
        name (str): Nome do item.
        price (float): Preço do item.
        is_offer (str): Indica se o item está em oferta (opcional).
    """

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_offer = Column(String, nullable=True)

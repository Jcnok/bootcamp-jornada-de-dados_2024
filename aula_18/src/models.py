from db import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func


class Pokemon(Base):
    """Modelo para representar os dados de um Pokémon."""

    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, doc="O nome do Pokémon.")
    type = Column(String, doc="O tipo do Pokémon.")
    created_at = Column(
        DateTime, default=func.now(), doc="O timestamp de quando o registro foi criado."
    )

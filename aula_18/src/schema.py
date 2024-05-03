from pydantic import BaseModel


class PokemonSchema(BaseModel):
    """Esquema Pydantic para representar os dados de um Pokémon."""

    name: str
    type: str

    class Config:
        """Configuração do esquema Pydantic."""

        from_attributes = True

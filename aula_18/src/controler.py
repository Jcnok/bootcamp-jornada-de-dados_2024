import requests
from db import Base, SessionLocal, engine
from models import Pokemon
from schema import PokemonSchema

# Cria as tabelas no banco de dados, se ainda não existirem
Base.metadata.create_all(bind=engine)


def fetch_pokemon_data(pokemon_id: int):
    """Função para buscar os dados de um Pokémon da API."""
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        types = ", ".join(type["type"]["name"] for type in data["types"])
        return PokemonSchema(name=data["name"], type=types)
    else:
        return None


def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    """Função para adicionar os dados de um Pokémon ao banco de dados."""
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon

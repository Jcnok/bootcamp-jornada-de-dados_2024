import random
import time

from controler import add_pokemon_to_db, fetch_pokemon_data


def main():
    """Função principal para iniciar a coleta de dados dos Pokémon."""
    while True:
        pokemon_id = random.randint(1, 350)  # Gera um ID aleatório entre 1 e 350
        pokemon_schema = fetch_pokemon_data(pokemon_id)
        if pokemon_schema:
            print(f"Adicionando {pokemon_schema.name} ao banco de dados.")
            add_pokemon_to_db(pokemon_schema)
        else:
            print(f"Não foi possível obter dados para o Pokémon com ID {pokemon_id}.")
        time.sleep(10)


if __name__ == "__main__":
    main()

#3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# Cria um dicionário com informações do livro
livro = {
    "titulo": "Inteligência Artificial",
    "autor": "Kai-Fu Lee",
    "ano_publicacao": 2019
}

# Imprime cada informação do livro
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

import requests

# Definindo a URL base da API
base_url = "http://localhost:8000"


# Função para imprimir a resposta de uma requisição
def print_response(response):
    print("Status code:", response.status_code)
    print("Response body:", response.json())
    print()


# Exemplo de adição de livro (CREATE)
livro_data = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "disponivel": True,
}
response = requests.post(f"{base_url}/livros/", json=livro_data)
print("Adicionar livro:")
print_response(response)

# Exemplo de consulta de livro por autor (READ)
autor = "Machado de Assis"
response = requests.get(f"{base_url}/livros/{autor}")
print("Consultar livro por autor:")
print_response(response)

# Exemplo de atualização de disponibilidade de livro (UPDATE)
livro_id = 1  # Supondo que o ID do livro a ser atualizado seja 1
response = requests.put(f"{base_url}/livros/{livro_id}?disponivel=false")
print("Atualizar disponibilidade do livro:")
print_response(response)

# Exemplo de remoção de livro (DELETE)
response = requests.delete(f"{base_url}/livros/{livro_id}")
print("Remover livro:")
print_response(response)

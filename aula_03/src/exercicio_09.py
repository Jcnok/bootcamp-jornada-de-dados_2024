# Exercício 9: Extração de Subconjuntos de Dados
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Extrair apenas os números pares usando uma compreensão de lista
pares = [numero for numero in numeros if numero % 2 == 0]

# Alternativamente, você também pode usar a função filter()
# pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimir os números pares
print("Números pares:", pares)

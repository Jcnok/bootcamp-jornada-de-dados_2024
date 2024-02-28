# Exercício 7: Normalização de Dados
# Lista de números de exemplo
numeros = [10, 20, 30, 40, 50]

# Calcula o valor mínimo e máximo da lista
minimo = min(numeros)
maximo = max(numeros)

# Normaliza os números para a escala de 0 a 1
numeros_normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# Imprime os números normalizados
print("Números normalizados:", numeros_normalizados)

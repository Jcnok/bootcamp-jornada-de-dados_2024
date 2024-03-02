#1. [Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.]
# Cria uma lista de números de 1 a 10
numeros = list(range(1, 11))
# Loop para imprimir cada número e seu quadrado
for numero in numeros:
    quadrado = numero ** 2
    print(f"{numero} elevado ao quadrado é: {quadrado}")

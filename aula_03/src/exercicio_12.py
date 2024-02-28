# Exercício 12: Validação de Entrada
# Definir o intervalo específico
inicio_intervalo = 1
fim_intervalo = 10

# Loop para solicitar o número até que a entrada seja válida
while True:
    try:
        numero = int(input(f"Digite um número entre {inicio_intervalo} e {fim_intervalo}: "))
        if inicio_intervalo <= numero <= fim_intervalo:
            print("Número válido:", numero)
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

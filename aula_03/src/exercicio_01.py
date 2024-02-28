# Exercício 1: Verificação de Qualidade de Dados
try:
    # Entrada dos valores de quantidade e preço
    quantidade = float(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    # Verificação se ambos os valores são positivos
    if quantidade > 0 and preco > 0:
        print("Dados válidos")
    else:
        print("Dados inválidos")
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido para quantidade e preço.")

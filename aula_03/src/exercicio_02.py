#Exercício 2: Classificação de Dados de Sensor
try:
    # Entrada da temperatura
    temperatura = float(input("Digite a temperatura em °C: "))

    # Classificação da temperatura
    if temperatura < 18:
        print("Baixa")
    elif 18 <= temperatura <= 26:
        print("Normal")
    else:
        print("Alta")
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido para a temperatura.")

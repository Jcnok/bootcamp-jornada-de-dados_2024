print("="*5,"Cálculo da conversão de Celsius para fahrenheit","="*5)
try:
    celsius = float(input("digite um número em graus celsius:"))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius} Graus Celsius equivale a: {round(fahrenheit,2)} graus fahrenheit")
except ValueError:
    print("Digite um número válido para temperatura!")
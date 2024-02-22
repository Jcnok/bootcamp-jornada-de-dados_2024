try:
    numero = int(input("digite um número inteiro:"))
    if numero == 0:
        print("o número é zero")
    elif numero < 0: 
        print("o número é negativo")
    else:
        print("o número é positivo")
    resto = numero % 2
    if resto == 0:
        print(f"o número é par")
    else:
        print(f"o número é impar")    

except ValueError as e:
    print(e)
    print("Certifique-se de que o número inserido é do tipo inteiro.")
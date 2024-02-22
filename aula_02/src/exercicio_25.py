try:

    lista = input("digite uma sequência de números separado por vírgula:")
    lista_ok = [int(x) for x in lista.split(',')]
    print(f"lista dos números inteiros: {lista_ok}")

except ValueError as e:
    print(e)
    print("Digite uma sequência de números inteiros válidos separado por vírgula")
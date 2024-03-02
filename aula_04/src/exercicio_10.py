# 10. Divisão de Dados em Grupos: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
lista = [ 1, 2, 3, 5, 9, 8 , 15, 36]
lista_pares = []
lista_impares = []
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print(f"lista de pares = {lista_pares} \n")
print(f"lista de ímpares = {lista_impares}")
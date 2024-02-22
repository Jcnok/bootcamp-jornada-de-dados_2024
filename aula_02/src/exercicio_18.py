print("-"*5,"inverte boleano","-"*5) 
valor = input("insira 'True' ou 'False':").lower()
if valor == 'true':
    booleano = True
else:
    booleano = False

booleano_invertido = not booleano
print(f"O resultado de {booleano} invertido é: {booleano_invertido}!")
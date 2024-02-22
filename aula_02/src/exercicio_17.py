print("-"*5,"compara boleanos com OR","-"*5) 
bool1 = input("insira 'True' ou 'False':").lower()
bool2 = input("insira um segundo 'True' ou 'False' para comparação:").lower()
resultado = bool1 or bool2
print(f"O resultado de {bool1} or {bool2} é: {resultado}!")
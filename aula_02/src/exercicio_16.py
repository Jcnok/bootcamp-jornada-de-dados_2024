print("-"*5,"compara boleanos com AND","-"*5) 
bool1 = input("insira 'True' ou 'False':").lower()
bool2 = input("insira um segundo 'True' ou 'False' para comparação:").lower()
resultado = bool1 and bool2
print(f"O resultado de {bool1} and {bool2} é: {resultado}!")
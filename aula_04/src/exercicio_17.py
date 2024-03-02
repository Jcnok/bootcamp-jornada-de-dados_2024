# 17.Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário. 
# algoritmo de Sieve of Eratosthenes
def num_primo(num):
    if num <= 1: 
        return False 
    elif num <= 3:
        return True
    elif (num % 2 == 0) or (num % 3 == 0):
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
          return False
        i += 6
    return True
    
numero = int(input("Digite um número: "))

if num_primo(numero):
  print(f"O número {numero} é primo.")
else:
  print(f"O número {numero} não é primo.")
    
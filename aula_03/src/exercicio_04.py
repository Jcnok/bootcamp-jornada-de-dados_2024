#Exercício 4: Validação de Dados de Entrada
import re

# Entrada dos dados do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

# Validação da idade
if idade < 18:
    print("Idade menor que 18 anos.")
elif idade > 65:
    print("Idade maior que 65 anos.")
else:
    # Validação do email
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Email inválido.")
    else:
        print("Dados de usuário válidos.")

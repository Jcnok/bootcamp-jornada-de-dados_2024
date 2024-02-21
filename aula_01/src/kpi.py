# 1) Solicita ao usuário que digite seu nome
nome = str(input("Digite seu Nome:"))
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salary = float(input("Digite o valor do salario mensal:"))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do seu Bônus:"))
# 4) Calcule o valor do bônus final
kpi_bonus = 1000 + salary * bonus
# 5) Imprima cálculo do KPI para o usuário
print(f"O cálculo do bônus: 1000 + salario + bonus = R$ {kpi_bonus:,.2f}.\n")
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, considerando seu salário de: R$ {salary:,.2f}, o total com bônus é de R$ {kpi_bonus:,.2f}.\n")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
'''
1. Não existe nenhuma excecão para incluir qualquer valor na variável nome.
2. Salário e Bônus aceitam valores negativos.
3. Bug detectado ao inserir um valor tipo string nos campos salário e bônus.
'''

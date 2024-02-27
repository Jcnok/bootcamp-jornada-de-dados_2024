try:
    # Solicita ao usuário que insira seu nome
    nome = input("Digite seu nome: ").strip()
    
    # Verifica se o nome está vazio ou contém números
    if not nome:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")

    # Solicita ao usuário que insira o valor do salário e valida
    salario = float(input("Digite o valor do seu salário: "))
    if salario <= 0:
        print("Por favor, digite um valor positivo para o salário.")
        raise ValueError

    # Solicita ao usuário que insira o valor do bônus em porcentagem
    bonus_recebido = float(input("Digite o percentual do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
        raise ValueError

    # Calcula o total
    kpi = 1000 + salario * bonus_recebido  

    # Imprime as informações para o usuário
    print(f"{nome}, considerando seu salário de R${salario:.2f} o total com bônus é de R${kpi:.2f}.")
except ValueError as e:
    print("Erro:", e)
except Exception as e:
    print("Ocorreu um erro:", e)

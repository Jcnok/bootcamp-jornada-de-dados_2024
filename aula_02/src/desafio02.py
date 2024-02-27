def solicitar_nome() -> str:
    """
    Solicita ao usuário que insira seu nome.

    Retorna:
        str: O nome inserido pelo usuário.
    """
    try:
        nome = input("Digite seu nome: ").strip()

        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        
        return nome
    except ValueError as e:
        print("Erro ao inserir nome:", e)
        return solicitar_nome()


def solicitar_salario() -> float:
    """
    Solicita ao usuário que insira o valor do salário.

    Retorna:
        float: O valor do salário inserido pelo usuário.
    """
    try:
        salario = float(input("Digite o valor do seu salário: "))

        if salario <= 0:
            print("Por favor, digite um valor positivo para o salário.")
            return solicitar_salario()

        return salario
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        return solicitar_salario()


def solicitar_bonus() -> float:
    """
    Solicita ao usuário que insira o valor do bônus recebido.

    Retorna:
        float: O valor do bônus inserido pelo usuário.
    """
    try:
        bonus_recebido = float(input("Digite o valor do bônus recebido: "))

        if bonus_recebido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
            return solicitar_bonus()

        return bonus_recebido
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
        return solicitar_bonus()


def main():
    """
    Função principal do programa.
    """
    try:
        # Solicita e valida o nome
        nome = solicitar_nome()

        # Solicita e valida o salário
        salario = solicitar_salario()

        # Solicita e valida o bônus
        bonus_recebido = solicitar_bonus()

        # Calcula o total
        kpi = 1000 + salario * bonus_recebido  

       
        # Imprime as informações para o usuário
        
        print(f"{nome}, considerando seu salário de R${salario:.2f} o total com bônus é de R${kpi:.2f}.")
    except Exception as e:
        print("Ocorreu um erro:", e)


if __name__ == "__main__":
    main()

# 21.Desafio será tipar o desafio da aula 03 
from typing import Dict

def solicitar_dados_usuario() -> Dict[str, float]:
    """
    Solicita ao usuário que insira seu nome, salário e percentual de bônus.
    
    Returns:
        Dict[str, float]: Um dicionário contendo o nome, salário e bônus recebido.
    """
    while True:
        try:
            nome = input("Digite seu nome: ").strip()
            if not nome:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            
            salario = float(input("Digite o valor do seu salário: "))
            if salario <= 0:
                print("Por favor, digite um valor positivo para o salário.")
                raise ValueError
            
            bonus_recebido = float(input("Digite o percentual do bônus recebido: "))
            if bonus_recebido < 0:
                print("Por favor, digite um valor positivo para o bônus.")
                raise ValueError
            
            return {'nome': nome, 'salario': salario, 'bonus_recebido': bonus_recebido}
        
        except ValueError as e:
            print("Erro:", e)

def calcular_kpi(dados: Dict[str, float]) -> float:
    """
    Calcula o indicador de desempenho (KPI) com base nos dados fornecidos.

    Args:
        dados (Dict[str, float]): Um dicionário contendo o nome, salário e bônus recebido.

    Returns:
        float: O valor do KPI calculado.
    """
    return 1000 + dados['salario'] * dados['bonus_recebido']

def imprimir_informacoes(dados: Dict[str, float], kpi: float) -> None:
    """
    Imprime as informações do usuário e o valor do KPI.

    Args:
        dados (Dict[str, float]): Um dicionário contendo o nome, salário e bônus recebido.
        kpi (float): O valor do indicador de desempenho (KPI).
    """
    print(f"{dados['nome']}, considerando seu salário de R${dados['salario']:.2f}, o total com bônus é de R${kpi:.2f}.")

def main() -> None:
    """
    Função principal do programa.
    """
    while True:
        try:
            dados_usuario = solicitar_dados_usuario()
            kpi = calcular_kpi(dados_usuario)
            imprimir_informacoes(dados_usuario, kpi)
            break
        except Exception as e:
            print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()

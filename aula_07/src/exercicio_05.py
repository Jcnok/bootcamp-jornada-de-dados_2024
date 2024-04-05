# 5. Calcular desvio padrão de uma lista:
from typing import List


def calcular_desvio_padrao(valores: List[float]) -> float:
    """
    Função para calcular o desvio padrão de uma lista de valores.

    Args:
        valores (List[float]): Uma lista de valores numéricos.

    Returns:
        float: O desvio padrão dos valores na lista.
    """
    # Calcula a média dos valores na lista
    media = sum(valores) / len(valores)
    # Calcula a variância dos valores na lista
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    # Retorna a raiz quadrada da variância, que é o desvio padrão
    return variancia**0.5

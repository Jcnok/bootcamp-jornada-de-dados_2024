# Calcular a média de valores em uma lista:
from typing import List


def calcular_media(valores: List[float]) -> float:
    """
    Função para calcular a média de uma lista de valores.

    Args:
        valores (List[float]): Uma lista de valores numéricos.

    Returns:
        float: A média dos valores na lista.
    """
    # Soma todos os valores na lista
    soma = sum(valores)
    # Calcula a média dividindo a soma pelo número de valores na lista
    media = soma / len(valores)
    return round(media, 2)

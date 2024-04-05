# 2.Filtrar dados acima de um limite:
from typing import List


def filtrar_dados_limite(valores: List[float], limite: float) -> List[float]:
    """
    Função para filtrar valores em uma lista que estão acima de um determinado limite.

    Args:
        valores (List[float]): Uma lista de valores numéricos.
        limite (float): O limite para filtrar os valores.

    Returns:
        List[float]: Uma lista contendo apenas os valores acima do limite.
    """
    # Inicializa uma lista vazia para armazenar os valores filtrados
    resultado = []
    # Itera sobre cada valor na lista de entrada
    for valor in valores:
        # Verifica se o valor atual é maior que o limite
        if valor > limite:
            # Se for, adiciona o valor à lista de resultados
            resultado.append(valor)
    # Retorna a lista de valores filtrados
    return resultado

# 3. Contar valores únicos em uma lista:
from typing import List


def contar_valores_unicos(lista: List[int]) -> int:
    """
    Função para contar o número de valores únicos em uma lista.

    Args:
        lista (List[int]): Uma lista de valores inteiros.

    Returns:
        int: O número de valores únicos na lista.
    """
    # Converte a lista para um conjunto (set) para eliminar valores duplicados
    valores_unicos = set(lista)
    # Retorna o número de elementos no conjunto, que corresponde ao número de valores únicos
    return len(valores_unicos)

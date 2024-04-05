# 6. Encontrar Valores Ausentes em uma Sequência:
from typing import List


def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    """
    Função para encontrar valores ausentes em uma sequência de números inteiros.

    Args:
        sequencia (List[int]): Uma sequência de números inteiros.

    Returns:
        List[int]: Uma lista contendo os valores ausentes na sequência.
    """
    # Cria um conjunto completo contendo todos os números no intervalo da sequência
    completo = set(range(min(sequencia), max(sequencia) + 1))
    # Retorna os valores ausentes encontrando a diferença entre o conjunto completo e o conjunto da sequência
    return list(completo - set(sequencia))

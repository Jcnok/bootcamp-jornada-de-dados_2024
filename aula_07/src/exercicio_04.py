# 4.Converter celsius para Fahrenheit em uma lista:
from typing import List


def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    """
    Função para converter uma lista de temperaturas de Celsius para Fahrenheit.

    Args:
        temperaturas_celsius (List[float]): Uma lista de temperaturas em graus Celsius.

    Returns:
        List[float]: Uma lista de temperaturas convertidas para Fahrenheit.
    """
    # Utiliza uma list comprehension para converter cada temperatura de Celsius para Fahrenheit
    temperaturas_fahrenheit = [(9 / 5) * temp + 32 for temp in temperaturas_celsius]
    return temperaturas_fahrenheit

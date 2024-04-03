# Exemplo de arquivo desorganizado com imports
import math
import os
import site


def calcular_area_circulo(raio):
    """
    Função para calcular a área de um círculo.
    """
    return math.pi * raio**2


def diretorio_atual():
    """
    Função para informar o diretório atual.
    """
    return os.getcwd()


def ambiente_atual():
    """
    Informa o ambiente de desenvolvimento atual.
    """
    return site.getsitepackages()


if __name__ == "__main__":
    diretorio_atual()

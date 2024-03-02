# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
def obter_chaves_ordenadas(dicionario):
  """
  Retorna uma lista de chaves ordenadas de um dicionário.

  Argumentos:
    dicionario: O dicionário a ser usado.

  Retorno:
    Uma lista de chaves ordenadas.
  """
  chaves = list(dicionario.keys())
  chaves.sort()
  return chaves

dicionario = {"b": 6, "d": 2, "a": 3, "e": 4, "c": 5}

chaves_ordenadas = obter_chaves_ordenadas(dicionario)

print(f"Chaves ordenadas: {chaves_ordenadas}")

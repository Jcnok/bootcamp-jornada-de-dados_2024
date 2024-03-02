#19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def encontrar_pares(lista, numero):
  """
  Encontra todas as combinações de pares em uma lista que somam um número dado.

  Argumentos:
    lista: A lista de números a ser pesquisada.
    numero: O número que a soma dos pares deve ser igual.

  Retorno:
    Uma lista de pares que somam o número dado.
  """
  pares = []
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] + lista[j] == numero:
        pares.append((lista[i], lista[j]))

  return pares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = 10

pares = encontrar_pares(lista, numero)

print(f"Pares que somam {numero}: {pares}")

# 14. Extração de Chaves e Valores: Dado um dicionário, criar listas separadas para suas chaves e valores.
estoque = {
  "produto1": 10,
  "produto2": 0,
  "produto3": 5,
}
lista_chave = list(estoque.keys())
lista_valor = list(estoque.values())
print(f"chave:{lista_chave}")
print(f"valor:{lista_valor}")
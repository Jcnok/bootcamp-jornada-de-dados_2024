# 13. Filtragem de Dados em Dicionário: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {
  "produto1": {"quantidade": 10},
  "produto2": {"quantidade": 0},
  "produto3": {"quantidade": 5},
}
for produto in estoque:
    if (estoque[produto]['quantidade']) > 0:
        print(f"Produto:{produto} em estoque:{estoque[produto]['quantidade']}")  

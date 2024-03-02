# 11. Atualização de Dados:Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
  {"nome": "Camiseta","preco": 50.00},
  {"nome": "Calça Jeans","preco": 100.00},
  {"nome": "Tênis", "preco": 150.00},
  {"nome": "Casaco", "preco": 200.00},
  {"nome": "Vestido", "preco": 250.00},
]

nome_produto = 'Camiseta'
novo_preco = 60.00
for produto in produtos:
    if (produto['nome'] == nome_produto):
        produto['preco'] = novo_preco
        print(f"produto {produto['nome']} foi atualizado para: R$ {produto['preco']:.2f}")
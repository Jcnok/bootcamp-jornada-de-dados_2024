# Exercício 10: Agregação de Dados por Categoria
# Conjunto de registros de vendas (exemplo)
registros_vendas = [
    {'categoria': 'Eletrônicos', 'valor': 1000},
    {'categoria': 'Roupas', 'valor': 500},
    {'categoria': 'Eletrônicos', 'valor': 1500},
    {'categoria': 'Alimentos', 'valor': 800},
    {'categoria': 'Roupas', 'valor': 700},
    {'categoria': 'Alimentos', 'valor': 1200}
]

# Dicionário para armazenar o total de vendas por categoria
total_vendas_por_categoria = {}

# Calcular o total de vendas por categoria
for venda in registros_vendas:
    categoria = venda['categoria']
    valor_venda = venda['valor']
    total_vendas_por_categoria[categoria] = total_vendas_por_categoria.get(categoria, 0) + valor_venda

# Imprimir o total de vendas por categoria
print("Total de vendas por categoria:")
for categoria, total_vendas in total_vendas_por_categoria.items():
    print(f"{categoria}: R${total_vendas:.2f}")

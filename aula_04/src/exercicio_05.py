#5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
preco_produto = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = 0
for lista in lista_compras:
    if lista in preco_produto:
        total += preco_produto[lista]
        print(f"produto: {lista.ljust(10)}    -------------- R$ {preco_produto[lista]:.2f}")
    else:
        print(f"produto: {lista.ljust(10)}    -------------- em falta!")

print(f"Total:   ---------------------------- R$ {total:.2f}")
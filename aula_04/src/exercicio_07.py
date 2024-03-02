# 7. Filtragem de Dados: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [10, 20, 45, 18, 12, 16, 5]
resultado = [x for x in idades if x >= 18]
# outra forma list(filter(lambda x: x >= 18, idades))
print(f"Idades maiores ou iguais a 18:{resultado}")
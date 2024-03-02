# 12. Fusão de Dicionários: Dado dois dicionários, fundi-los em um único dicionário.
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
# outra forma de fazer: dict = dicionario1 | dicionario2
dicionario1.update(dicionario2)
print(dicionario1)
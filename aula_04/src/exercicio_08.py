# 8. Ordenação Personalizada: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas =[
  {"nome": "Ana", "idade": 25},
  {"nome": "Pedro", "idade": 30},
  {"nome": "Maria", "idade": 22},
  {"nome": "Julio", "idade": 28},
]

pessoas_ordenadas = list(sorted(pessoas, key=lambda pessoa: pessoa["nome"]))
print(f"lista ordenada por nome:{pessoas_ordenadas}")
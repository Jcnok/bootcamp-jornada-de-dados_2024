#6. Eliminação de Duplicatas: Dada uma lista de emails, remover todos os duplicados.
emails = ["joaosilva@email.com", "mariagomes@email.com", "pedrodutra@email.com","joaosilva@email.com",
          "marialopes@email.com", "carlosbarbosa@email.com", "anagomes@email.com","carlosbarbosa@email.com"]
print(f"{'='*10}Os emails duplicados foram removidos com sucesso!{'='*10}\n{list(set(emails))}")
# 15. Contagem de Frequência de Itens: Dada uma string, contar a frequência de cada caractere usando um dicionário.
string = "A única maneira de fazer um ótimo trabalho é amar o que você faz."
conta_caractere = {}
for caractere in string:
    if caractere in conta_caractere:
        conta_caractere[caractere] +=1
    else:
        conta_caractere[caractere] = 1
print(conta_caractere)
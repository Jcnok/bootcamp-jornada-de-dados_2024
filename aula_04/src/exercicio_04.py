# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
string = "A única maneira de fazer um ótimo trabalho é amar o que você faz."
conta_caractere = {}
for caractere in string:
    if caractere in conta_caractere:
        conta_caractere[caractere] +=1
    else:
        conta_caractere[caractere] = 1
print(conta_caractere)
    
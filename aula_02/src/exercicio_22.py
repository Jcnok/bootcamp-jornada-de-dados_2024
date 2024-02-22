print("="*5,"Verifica se uma palavra ou frase é um palíndromo","="*5)
try:
    texto = input("insira uma frase ou palavra':")     
    #convertendo todo o texto em minúsculo
    texto = texto.lower()
    #Iterando sobre o texto para remover pontuações e espaços
    texto = ''.join([x for x in texto if x.isalnum()])
    #Verifica se a frase é um palíndromo
    resposta = texto == texto[::-1]   
    if resposta:
        print("o texto é um palíndromo!")
    else:
        print("o textto não é um palíndromo!")
except ValueError:
    print("entrada inválida")
    
    
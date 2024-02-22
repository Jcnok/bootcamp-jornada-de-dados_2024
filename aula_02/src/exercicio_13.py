print("-"*5,"Remove espaços no início e final de uma frase.", "-"*5)
frase = str(input("Insira uma frase com espaço no início e final:"))
frase_sem_espaco = frase.strip()
print(frase_sem_espaco)
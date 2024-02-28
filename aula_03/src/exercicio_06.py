# Exercício 6: Contagem de Palavras em Textos
# Texto de exemplo
texto = "Python é uma linguagem de programação de alto nível e de uso geral, que pode ser utilizada para uma ampla variedade de tarefas. Python é conhecida por sua sintaxe simples e legibilidade de código."

# Transforma o texto em minúsculas e separa as palavras
palavras = texto.lower().split()

# Cria um dicionário para armazenar a contagem de cada palavra única
contagem_palavras = {}

# Conta quantas vezes cada palavra única aparece no texto
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Imprime a contagem de cada palavra única
for palavra, contagem in contagem_palavras.items():
    print(f"A palavra '{palavra}' aparece {contagem} vez(es) no texto.")


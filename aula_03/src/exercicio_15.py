# Exercício 15: Processamento de Dados com Condição de Parada
# Lista de itens
lista = [10, 20, 30, 40, 50, 60, 70, "parar", 80, 90, 100]

# Inicializa o índice
indice = 0

# Loop para processar os itens da lista
while indice < len(lista):
    item = lista[indice]

    # Verifica se o item é o valor específico que indica a parada
    if item == "parar":
        print("Encontrou o valor 'parar'. Parando o processamento.")
        break

    # Processa o item
    print("Processando item:", item)

    # Atualiza o índice para avançar para o próximo item
    indice += 1

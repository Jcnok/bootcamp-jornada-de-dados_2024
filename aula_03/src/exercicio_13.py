# Exercício 13: Consumo de API Simulado
# Número total de páginas (simulação)
paginas_totais = 3  

# Se não houver páginas, exibe uma mensagem e sai do loop
if paginas_totais <= 0:
    print("Não há páginas para processar.")
else:
    # Inicializa a página atual
    pagina_atual = 1
    
    # Loop para processar cada página de dados
    while pagina_atual <= paginas_totais:
        print(f"Processando página {pagina_atual} de {paginas_totais}")

        # Simulação de processamento de dados
        print(f"Dados da página {pagina_atual}:")
        for i in range(1, 6):
            print(f"Dado {i}")

        # Atualiza a página atual
        pagina_atual += 1

print("Todas as páginas foram processadas.")


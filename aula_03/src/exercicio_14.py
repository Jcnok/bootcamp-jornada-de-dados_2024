# Exercício 14: Tentativas de Conexão
# Simulação de tentativas de reconexão
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    tentativas += 1
    print(f"Tentativa de reconexão {tentativas}")

    # Simulação de conexão ao serviço
    conexao_sucesso = False  # Simulação de falha na conexão

    if conexao_sucesso:
        print("Conexão bem-sucedida.")
        break
    else:
        print("Falha na conexão. Tentando novamente.")

# Verifica se atingiu o limite de tentativas
if tentativas == limite_tentativas:
    print("Limite de tentativas atingido. Não foi possível reconectar ao serviço.")

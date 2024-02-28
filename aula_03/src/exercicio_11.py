# Exercício 11:  Leitura de Dados até Flag
# Palavra-chave específica
palavra_chave = "sair"

# Lista para armazenar os dados de entrada
dados = []

# Loop para ler os dados de entrada
while True:
    entrada = input("Digite um dado (ou 'sair' para encerrar): ")
    if entrada.lower() == palavra_chave:
        break
    dados.append(entrada)

# Imprimir os dados lidos
print("Dados lidos:")
for dado in dados:
    print(dado)

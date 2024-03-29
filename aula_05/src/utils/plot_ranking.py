import csv
import matplotlib.pyplot as plt

def plot_ranking_tempo_execucao(arquivo_csv):
    # Leitura dos dados do arquivo CSV
    dados = []

    with open(arquivo_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nome_funcao = row[0]
            tempo = row[1].split()  # Separa minutos e segundos
            if len(tempo) == 2 and tempo[1] == 'segundos':  # Se houver apenas segundos
                tempo_total = float(tempo[0])
            elif len(tempo) == 4:  # Se houver minutos e segundos
                minutos = float(tempo[0])
                segundos = float(tempo[2])
                tempo_total = minutos * 60 + segundos  # Converte minutos para segundos
            else:
                raise ValueError(f'Formato de tempo inválido: {row[1]}')
            dados.append((nome_funcao, tempo_total))

    # Ordena os dados pelo tempo de execução
    dados_ordenados = sorted(dados, key=lambda x: x[1])

    # Extrai os nomes das funções e os tempos de execução ordenados
    nomes_funcoes_ordenados = [item[0] for item in dados_ordenados]
    tempos_execucao_ordenados = [item[1] for item in dados_ordenados]

    # Plotagem do gráfico
    plt.figure(figsize=(10, 6))
    plt.barh(nomes_funcoes_ordenados, tempos_execucao_ordenados, color='skyblue')
    plt.xlabel('Tempo de Execução (segundos)')
    plt.ylabel('Função')
    plt.title('Tempo de Execução das Funções (Ordenado)')
    plt.grid(axis='x')
    plt.tight_layout()

    # Adicionando os valores nas barras
    for i, valor in enumerate(tempos_execucao_ordenados):
        plt.text(valor, i, f'{valor:.2f} s', va='center')

    # Exibindo o gráfico
    # plt.show()
    plt.savefig('./img/ranking.png')
    print('Gráfico salvo com sucesso na pasta:img/ranking.png')

# Exemplo de uso da função
if __name__ == "__main__":
    arquivo_csv = './data/tempos_execucao.csv'
    plot_ranking_tempo_execucao(arquivo_csv)

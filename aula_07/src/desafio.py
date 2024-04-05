# desafio - Análise de Vendas de Produtos
import csv
from typing import Dict, List


# Função para ler o arquivo CSV e carregar os dados
def ler_csv(nome_arquivo: str) -> List[Dict[str, str]]:
    with open(nome_arquivo, newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = [linha for linha in leitor]
    return dados


# Função para processar os dados em um dicionário por categoria
def processar_dados(dados: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    categorias = {}
    for linha in dados:
        categoria = linha["Categoria"]
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(
            {
                "Produto": linha["Produto"],
                "Quantidade": int(linha["Quantidade"]),
                "Venda": float(linha["Venda"]),
            }
        )
    return categorias


# Função para calcular o total de vendas por categoria
def calcular_vendas_categoria(
    categorias: Dict[str, List[Dict[str, str]]]
) -> Dict[str, float]:
    total_vendas = {}
    for categoria, produtos in categorias.items():
        total_vendas[categoria] = sum(
            produto["Quantidade"] * produto["Venda"] for produto in produtos
        )
    return total_vendas


# Função principal
def main():
    # Ler o arquivo CSV
    dados = ler_csv("data/vendas.csv")

    # Processar os dados
    categorias = processar_dados(dados)

    # Calcular as vendas por categoria
    vendas_por_categoria = calcular_vendas_categoria(categorias)

    # Exibir os resultados
    for categoria, total_vendas in vendas_por_categoria.items():
        print(f'Total de vendas na categoria "{categoria}": R${total_vendas:.2f}')


if __name__ == "__main__":
    main()

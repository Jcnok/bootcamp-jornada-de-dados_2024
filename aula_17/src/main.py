from data_insertion import insert_data
from database import create_session
from models import Fornecedor, Produto
from sqlalchemy import func

# from sqlalchemy.orm import sessionmaker


def main():
    # Criando uma sessão para interagir com o banco de dados
    session = create_session()

    # Inserindo dados de exemplo
    insert_data()

    # Consulta para calcular o total de preço de produtos para cada fornecedor
    resultado = (
        session.query(Fornecedor.nome, func.sum(Produto.preco).label("total_preco"))
        .join(Produto, Fornecedor.id == Produto.fornecedor_id)
        .group_by(Fornecedor.nome)
        .all()
    )

    # Imprimindo os resultados
    for nome, total_preco in resultado:
        print(f"Fornecedor: {nome}, Total Preço: {total_preco}")


if __name__ == "__main__":
    main()

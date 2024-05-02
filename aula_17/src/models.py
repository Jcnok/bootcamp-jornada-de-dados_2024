from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Fornecedor(Base):
    """
    Classe que representa a tabela de Fornecedor.

    Atributos:
        id (int): Identificador único do fornecedor.
        nome (str): Nome do fornecedor.
        telefone (str): Número de telefone do fornecedor.
        email (str): Endereço de e-mail do fornecedor.
        endereco (str): Endereço físico do fornecedor.
        produtos (list): Lista dos produtos associados ao fornecedor.
    """

    __tablename__ = "fornecedores"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))
    produtos = relationship("Produto")


class Produto(Base):
    """
    Classe que representa a tabela de Produto.

    Atributos:
        id (int): Identificador único do produto.
        nome (str): Nome do produto.
        descricao (str): Descrição do produto.
        preco (int): Preço do produto.
        fornecedor_id (int): Chave estrangeira referenciando o fornecedor associado ao produto.
        fornecedor (Fornecedor): Relação com o fornecedor associado.
    """

    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    fornecedor = relationship("Fornecedor")

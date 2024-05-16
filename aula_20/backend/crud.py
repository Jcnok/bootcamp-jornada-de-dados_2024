from models import ProductModel
from schemas import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session


def get_product(db: Session, product_id: int):
    """
    Função para recuperar um produto específico.

    Args:
        db (Session): Sessão do banco de dados.
        product_id (int): ID do produto a ser recuperado.

    Returns:
        ProductModel: Objeto ProductModel representando o produto encontrado, ou None se não encontrado.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session):
    """
    Função para recuperar todos os produtos.

    Args:
        db (Session): Sessão do banco de dados.

    Returns:
        List[ProductModel]: Lista de objetos ProductModel representando todos os produtos encontrados.
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate):
    """
    Função para criar um novo produto.

    Args:
        db (Session): Sessão do banco de dados.
        product (ProductCreate): Objeto ProductCreate contendo os dados do novo produto.

    Returns:
        ProductModel: Objeto ProductModel representando o produto recém-criado.
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    """
    Função para deletar um produto.

    Args:
        db (Session): Sessão do banco de dados.
        product_id (int): ID do produto a ser deletado.

    Returns:
        ProductModel: Objeto ProductModel representando o produto deletado, ou None se não encontrado.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Função para atualizar um produto existente.

    Args:
        db (Session): Sessão do banco de dados.
        product_id (int): ID do produto a ser atualizado.
        product (ProductUpdate): Objeto ProductUpdate contendo os dados do produto atualizado.

    Returns:
        ProductModel: Objeto ProductModel representando o produto atualizado, ou None se não encontrado.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    return db_product

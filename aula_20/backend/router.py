from typing import List

from crud import (
    create_product,
    delete_product,
    get_product,
    get_products,
    update_product,
)
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schemas import ProductCreate, ProductResponse, ProductUpdate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Rota para criar um novo produto.

    Args:
        product (ProductCreate): Dados do novo produto.
        db (Session): Sessão do banco de dados.

    Returns:
        ProductResponse: Objeto ProductResponse representando o produto criado.
    """
    return create_product(db=db, product=product)


@router.get("/products/", response_model=List[ProductResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    """
    Rota para recuperar todos os produtos.

    Args:
        db (Session): Sessão do banco de dados.

    Returns:
        List[ProductResponse]: Lista de objetos ProductResponse representando todos os produtos.
    """
    products = get_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Rota para recuperar um produto específico.

    Args:
        product_id (int): ID do produto a ser recuperado.
        db (Session): Sessão do banco de dados.

    Returns:
        ProductResponse: Objeto ProductResponse representando o produto encontrado.

    Raises:
        HTTPException: Se o produto não for encontrado.
    """
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/products/{product_id}", response_model=ProductResponse)
def detele_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Rota para deletar um produto.

    Args:
        product_id (int): ID do produto a ser deletado.
        db (Session): Sessão do banco de dados.

    Returns:
        ProductResponse: Objeto ProductResponse representando o produto deletado.

    Raises:
        HTTPException: Se o produto não for encontrado.
    """
    db_product = delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    """
    Rota para atualizar um produto existente.

    Args:
        product_id (int): ID do produto a ser atualizado.
        product (ProductUpdate): Dados do produto atualizado.
        db (Session): Sessão do banco de dados.

    Returns:
        ProductResponse: Objeto ProductResponse representando o produto atualizado.

    Raises:
        HTTPException: Se o produto não for encontrado.
    """
    db_product = update_product(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

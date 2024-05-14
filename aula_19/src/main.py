from typing import List

import data
import models
from fastapi import Depends, FastAPI, HTTPException
from schema import Item, ItemCreate
from sqlalchemy.orm import Session

app = FastAPI()

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=data.engine)


@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(data.get_db)):
    """
    Cria um novo item no banco de dados.

    Args:
        item (ItemCreate): Os dados do item a ser criado.
        db (Session, opcional): Uma sessão do banco de dados.

    Returns:
        Item: O item criado.
    """
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(data.get_db)):
    """
    Retorna uma lista de itens do banco de dados.

    Args:
        skip (int, opcional): O número de itens a pular.
        limit (int, opcional): O número máximo de itens a retornar.
        db (Session, opcional): Uma sessão do banco de dados.

    Returns:
        List[Item]: Uma lista de itens.
    """
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(data.get_db)):
    """
    Retorna um item específico do banco de dados.

    Args:
        item_id (int): O ID do item a ser retornado.
        db (Session, opcional): Uma sessão do banco de dados.

    Returns:
        Item: O item especificado pelo ID.
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(data.get_db)):
    """
    Atualiza um item no banco de dados.

    Args:
        item_id (int): O ID do item a ser atualizado.
        item (ItemCreate): Os novos dados do item.
        db (Session, opcional): Uma sessão do banco de dados.

    Returns:
        Item: O item atualizado.
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(data.get_db)):
    """
    Deleta um item do banco de dados.

    Args:
        item_id (int): O ID do item a ser deletado.
        db (Session, opcional): Uma sessão do banco de dados.

    Returns:
        Item: O item deletado.
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item

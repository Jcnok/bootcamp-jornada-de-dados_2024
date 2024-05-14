from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    """
    Classe base para definição de atributos comuns de um item.

    Atributos:
        name (str): Nome do item.
        price (float): Preço do item.
        is_offer (Union[bool, None], opcional): Indica se o item está em oferta.
    """

    name: str
    price: float
    is_offer: Union[bool, None] = None


class ItemCreate(ItemBase):
    """
    Classe para criar um novo item.

    Herda os atributos da classe ItemBase.
    """

    pass


class Item(ItemBase):
    """
    Classe que representa um item.

    Herda os atributos da classe ItemBase e adiciona um identificador único (id).

    Atributos:
        id (int): Identificador único do item.
    """

    id: int

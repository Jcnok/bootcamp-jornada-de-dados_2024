from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveFloat, validator


class CategoriaBase(Enum):
    """
    Enum para definir as categorias possíveis do produto.
    """

    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"


class ProductBase(BaseModel):
    """
    Schema base para o modelo de produto.
    """

    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

    @validator("categoria")
    def check_categoria(cls, v):
        """
        Valida se a categoria informada é válida.
        """
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")


class ProductCreate(ProductBase):
    """
    Schema para criação de novos produtos.
    """

    pass


class ProductResponse(ProductBase):
    """
    Schema para a resposta da API quando um produto é criado ou retornado.
    """

    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    """
    Schema para atualizar um produto existente.
    """

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    @validator("categoria", pre=True, always=True)
    def check_categoria(cls, v):
        """
        Valida se a categoria informada é válida.
        """
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")

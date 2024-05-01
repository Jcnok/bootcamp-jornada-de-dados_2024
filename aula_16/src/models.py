# schemma livro
from typing import Optional

from sqlmodel import Field, SQLModel


class Livro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str
    ano_publicacao: int
    disponivel: bool = True

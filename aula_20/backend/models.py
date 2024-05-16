from database import Base
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func


class ProductModel(Base):
    """
    Modelo SQLAlchemy para a tabela 'products'.
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    categoria = Column(String, index=True)
    email_fornecedor = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)

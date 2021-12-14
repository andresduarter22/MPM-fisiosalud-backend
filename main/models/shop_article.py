"""
Shop Article
    Article_id: PK, AUTO, NOT_NULL, int
    Article_name: str, NOT_NULL
    Basic_info: str, NOT_NULL
    Number_of_items: int, NOT_NULL
    Price: float, NOT_NULL
    Currency: ENUM, NOT_NULL
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Enum

Base = declarative_base()


class ShopArticle(Base):
    __tablename__ = 'shop_article'
    article_id = Column(Integer, primary_key=True, nullable=False)
    article_name = Column(String(300), nullable=False)
    basic_info = Column(String(300), nullable=False)
    number_of_items = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(Enum, nullable=False)

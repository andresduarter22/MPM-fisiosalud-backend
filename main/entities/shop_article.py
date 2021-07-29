"""
Shop Article
    Article_id: PK, AUTO, NOT_NULL, int
    Article_name: str, NOT_NULL
    Basic_info: str, NOT_NULL
    Number_of_items: int, NOT_NULL
    Price: int, NOT_NULL
    Currency: ENUM, NOT_NULL
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class ShopArticle(Base):
    __tablename__ = 'shop_article'

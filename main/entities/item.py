"""
Item
    Item_id: PK, AUTO, NOT_NULL, int
    Area_id: FK, AUTO, NOT_NULL, int
    Item_name: str, NOT_NULL
    Item_description: TEXT
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'

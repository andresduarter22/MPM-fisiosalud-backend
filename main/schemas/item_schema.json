"""
Item
    Item_id: PK, AUTO, NOT_NULL, int
    Area_id: FK, AUTO, NOT_NULL, int
    Item_name: str, NOT_NULL
    Item_description: TEXT
"""

from main.models.working_area import WorkingArea
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey

Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True, nullable=False)
    area_id = Column(Integer, ForeignKey(WorkingArea.area_id), nullable=False)
    item_name = Column(String(100), nullable=False)
    item_description = Column(Text)

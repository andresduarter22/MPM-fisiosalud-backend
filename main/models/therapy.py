"""
Therapy
    Therapy_id: PK, AUTO, NOT_NULL, int
    Area_id: FK, AUTO, NOT_NULL, int
    Date: DATETIME, NOT_NULL
    Additional_info: TEXT
"""

from main.models.working_area import WorkingArea
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Therapy(Base):
    __tablename__ = 'therapy'
    Therapy_id = Column(Integer, primary_key=True)
    Area_id = Column(Integer, ForeignKey(WorkingArea.area_id), nullable=False)
    Date = Column(DateTime, nullable=False)
    Additional_info = Column(Text)

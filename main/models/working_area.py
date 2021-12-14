"""
Working Area
    Area_id: PK, AUTO, NOT_NULL, int
    Area_name: str, NOT_NULL
    Area_total_capacity: int
    Aviability: Boolean
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class WorkingArea(Base):
    __tablename__ = 'working_area'
    area_id = Column(Integer, primary_key=True)
    area_name = Column(String(50))
    area_total_capacity = Column(Integer)
    availability = Column(Boolean)
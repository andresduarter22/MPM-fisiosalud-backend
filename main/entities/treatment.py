"""
Treatment
    Treatment_id: PK, AUTO, NOT_NULL, int
    Patiten_id: FK, NOT_NULL, str
    Basic_info: TEXT, NOT_NULL
    Additional_info: TEXT
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Treatment(Base):
    __tablename__ = 'treatment'

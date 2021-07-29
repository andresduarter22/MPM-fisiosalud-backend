"""
Therapy
    Therapy_id: PK, AUTO, NOT_NULL, int
    Area_id: FK, AUTO, NOT_NULL, int
    Date: DATETIME, NOT_NULL
    Additional_info: TEXT
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Therapy(Base):
    __tablename__ = 'therapy'

"""
Document
    Document_id: PK, AUTO, NOT_NULL, int
    Patient_id: FK, AUTO, NOT_NULL, str
    Path: BLOB, NOT_NULL
    Additional_info: TEXT
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Boolean, BLOB, TEXT, VARCHAR, ForeignKey

Base = declarative_base()


class Document(Base):
    __tablename__ = 'document'

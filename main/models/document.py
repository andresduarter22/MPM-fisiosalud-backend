"""
Document
    Document_id: PK, AUTO, NOT_NULL, int
    Patient_id: FK, AUTO, NOT_NULL, str
    Path: BLOB, NOT_NULL
    Additional_info: TEXT
"""

from main.models.patient import Patient
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, BLOB, Text, String, ForeignKey

Base = declarative_base()


class Document(Base):
    __tablename__ = 'document'
    document_id = Column(Integer, nullable=False, primary_key=True)
    patient_id = Column(String(100), ForeignKey(Patient.patient_id))
    path = Column(BLOB, nullable=False)
    additional_info = Column(Text)

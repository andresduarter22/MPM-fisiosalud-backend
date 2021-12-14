"""
Treatment
    Treatment_id: PK, AUTO, NOT_NULL, int
    Patiten_id: FK, NOT_NULL, str
    Basic_info: TEXT, NOT_NULL
    Additional_info: TEXT
"""
from main.models.patient import Patient
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Text

Base = declarative_base()


class Treatment(Base):
    __tablename__ = 'treatment'
    treatment_id = Column(Integer, primary_key=True, nullable=False)
    patiten_id = Column(String(100), ForeignKey(Patient.id), nullable=False)
    basic_info = Column(Text, nullable=False)
    additional_info = Column(Text)

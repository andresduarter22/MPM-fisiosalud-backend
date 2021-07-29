"""
Patient
    Patient_id: PK, str, NOT_NULL
    Patient_name: str, NOT_NULL
    Patien_email: str, NOT_NULL
    Patient_nickname: str, NOT_NULL
    Patient_birthday: Date, NOT_NULL
    Patient_Phone_number: str, NOT_NULL
    Patient_address: str, NOT_NULL
    Reference_contact_name: str, NOT_NULL
    Reference_contact_number: str, NOT_NULL
    Reference_doctor: str
    Additional_info: TEXT
    Old_id: int
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Patient(Base):
    __tablename__ = 'patient'

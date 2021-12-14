"""
Contact List
    Contact_id: PK, AUTO, NOT_NULL, int
    Contact_name: str, NOT_NULL
    Contact_phone_number: str, NOT_NULL
    Contact_email: str
    Additional_info: str
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()


class ContactList(Base):
    __tablename__ = 'contact_list'
    contact_id = Column(Integer, primary_key=True, nullable=False)
    contact_name = Column(String(300), nullable=False)
    contact_phone_number = Column(String(20), nullable=False)
    contact_email = Column(String(50))
    additional_info = Column(Text)

"""
Contact List
    Contact_id: PK, AUTO, NOT_NULL, int
    Contact_name: str, NOT_NULL
    Contact_phone_number: str, NOT_NULL
    Contact_email: str
    Additional_info: str
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class ContactList(Base):
    __tablename__ = 'contact_list'

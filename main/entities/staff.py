"""
Staff
    Staff_id: PK, NOT_NULL, str
    Staff_name: str, NOT_NULL
    Staff_phone_number: int, NOT_NULL
    Staff_email: str, NOT_NULL
    Staff_role: ENUM (employee, receptionist, admin), NOT_NULL
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class Staff(Base):
    __tablename__ = 'staff'

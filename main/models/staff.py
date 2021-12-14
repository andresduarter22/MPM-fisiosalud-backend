"""
Staff
    Staff_id: PK, NOT_NULL, str
    Staff_name: str, NOT_NULL
    Staff_phone_number: int, NOT_NULL
    Staff_email: str, NOT_NULL
    Staff_role: ENUM (employee, receptionist, admin), NOT_NULL
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Enum
from main.utils.constants import StaffRole

Base = declarative_base()


class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column(String(100), primary_key=True, nullable=False)
    staff_name = Column(String(300), nullable=False)
    staff_phone_number = Column(String(20), nullable=False)
    staff_email = Column(String(50), nullable=False)
    staff_role = Column(Enum(StaffRole), nullable=False)

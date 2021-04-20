from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base

class ContactDetails(Base):
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String(length=12))
    address = Column(String(length=100))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    employee = relationship("Employee", backref=backref("contact_details", uselist=False))

    def __init__(self, phone_number, address, employee):
        self.phone_number = phone_number
        self.address = address
        self.employee = employee
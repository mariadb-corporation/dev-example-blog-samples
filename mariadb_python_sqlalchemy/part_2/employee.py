from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    firstname = Column(String(length=100))
    lastname = Column(String(length=100))
    active = Column(Boolean, default=True)
    department = relationship("Department", back_populates="employees")
    contact_details = relationship("ContactDetails", uselist=False, back_populates="employee")
    
    def __init__(self, firstname, lastname, department):
        self.firstname = firstname
        self.lastname = lastname
        self.department = department
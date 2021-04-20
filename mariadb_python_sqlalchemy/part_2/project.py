from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

projects_employees_association = Table(
    'projects_employees', Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id')),
    Column('employee_id', Integer, ForeignKey('employees.id'))
)

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    description = Column(String(length=500))
    due_date = Column(Date)
    employees = relationship("Employee", secondary=projects_employees_association)

    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
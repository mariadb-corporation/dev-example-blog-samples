from datetime import date

from base import Session, engine, Base
from employee import Employee
from project import Project 
from department import Department
from contact_details import ContactDetails

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()

# Create projects
project_1 = Project("Project 1", "Project 1 description", date(2021, 5, 31))
project_2 = Project("Project 2", "Project 2 description", date(2021, 4, 30))
project_3 = Project("Project 3", "Project 3 description", date(2021, 6, 15))

# Create departments
dept_marketing = Department("Marketing")
dept_engineering = Department("Engineering")

# Create employees
emp_john = Employee("John", "Locke", dept_marketing)
emp_kate = Employee("Kate", "Austin", dept_engineering)
emp_jack = Employee("Jack", "Shepherd", dept_marketing)
emp_ben = Employee("Ben", "Linus", dept_marketing)
emp_sun = Employee("Sun", "Kwan", dept_engineering)

# Add employees to projects
project_1.employees = [emp_john,emp_kate]
project_2.employees = [emp_jack,emp_ben,emp_sun]
project_3.employees = [emp_john,emp_kate,emp_jack,emp_ben,emp_sun]

# Create contact details
cd_john = ContactDetails("417 315 2531", "123 S Main ST", emp_john)
cd_kate = ContactDetails("417 315 2533", "124 S Main ST", emp_kate)
cd_jack = ContactDetails("417 315 2534", "125 S Main ST", emp_jack)
cd_ben = ContactDetails("417 315 2535", "126 S Main ST", emp_ben)
cd_sun = ContactDetails("417 315 2536", "127 S Main ST", emp_sun)


# Persist data
session.add(project_1)
session.add(project_2)
session.add(project_3)

session.add(dept_marketing)
session.add(dept_engineering)

session.add(cd_john)
session.add(cd_kate)
session.add(cd_jack)
session.add(cd_ben)
session.add(cd_sun)

session.commit()
session.close()
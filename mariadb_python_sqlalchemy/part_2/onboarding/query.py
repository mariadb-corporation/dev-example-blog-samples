from base import Session
from project import Project
from employee import Employee
from department import Department

session = Session()

# Get all projects
projects = session.query(Project).all()

print('### Projects ###')
for project in projects:
    print(project.name)
    for employee in project.employees:
        print(f'  - {employee.firstname} {employee.lastname} ({employee.department.name})')


# Get all departments
departments = session.query(Department).all()

print('### Departments ###')
for department in departments:
    print(department.name)
    for employee in department.employees:
        print(f'  - {employee.firstname} {employee.lastname}')

# John Lock projects
john_lock_projects = session.query(Project) \
                            .join(Employee, Project.employees) \
                            .filter(Employee.firstname == 'John') \
                            .all()

print('### John Locke projects ###')

for project in john_lock_projects:
    print(f'- {project.name}')
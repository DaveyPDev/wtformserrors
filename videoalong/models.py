from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models Go Below

class Project(db.Model):

    __tablename__ = 'projects'

    proj_code = db.Column(db.Text, primary_key = True)
    proj_name = db.Column(db.Text, nullable = False, unique = True)

    assignments = db.relationship('EmployeeProject', backref = '')

class EmployeeProject(db.Model):

    __tablename__ = 'employees_project'

    emp_id = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key = True)

    proj_code = db.Column(db.Text, db.ForeignKey('projects.proj_code'), primary_key = True)

    role = db.Column(db.Text)

    (emp_id = 1, proj_code = 'boat', role = 'Chair').employee


class Department(db.Model):
    """ Department Model """

    __tablename__ = 'departments'
    dept_code = db.column(db.Text, primary_key = True)
    dept_name = db.Column(db.Text, nullable = False, unique = True)
    phone = db.Column(db.Text)

    assignments = db.relationship('EmployeeProject', backref = 'employee')

    def __repr__(self):
        return f"<Department f{self.dept_code} {self.dept_name} {self.phone}>"

    employees = db.relationship('Employee')

class Employee(db.Model):
    """ Employee Model """

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False, unique = True)
    state = db.Column(db.Text, nullable = False, default = 'CA')
    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))
    
    dept = db.relationship('Department', backref='employees')

    assignments = db.relationship('EmployeeProject')

    projects = db.relationship('Project', second='employees_projects', backref='employees')

    def __repr__(self):
        return f"<Employee f{self.name} {self.state} {self.dept_code}>"

    def get_directory():
        all_emps = Employee.query.all()

        for emp in all_emps:
            if emp.dept is not None:
                print(emp.name, emp.dept.dept_name, emp.dept.phone)

            else:
                print(emp.name)
    
    def get_directory_join():
        directory = db.session.query(
            Employee.name, Department.dept_name, Department.phone).join(Department).all()

        for name, dept, phone in directory:
            print(name, dept, phone)

    def get_directory_join_class():
        directory = db.session.query(
            Employee, Department).join(Department).all()

        for emp, dept in directory:
            print(emp.name, dept.dept_name, dept.phone)

    def get_directory_all_join():
        directory = db.session.query(
            Employee.name, Department.dept_name, Department.phone).join(Department).outerjoin(Department).all()

        for name, dept, phone in directory:
            print(name, dept, phone)

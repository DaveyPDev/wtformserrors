from flask import Flask, request, render_template, redirect, flask, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Department, Employee, get_directory, get_directory_join, get_directory_join_class, get_directory_all_join, Project, EmployeeProject
from forms import AddSnackForm, EmployeeForm
from forms import UserForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'notsosecretkey123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/phones')
def list_phones():
    emps = Employee.query.all()
    return render_template('phone.html', emps=emps)

# @app.route("/emlpoyees/new", methods=["GET", "POST"])
# def add_employee():
#     """ Snack add Form """

#     form = AddEmployeeForm()
#     depts = [(d.dept_code, d.dept_name) for d in Department.query.all()]
#     form.dept_code.choices = depts

#     if form.validate_on_submit():
#         name = form.name.data
#         state = form.state.data
#         dept_code = form.dept_code.data
#         print(form.dept_code.data)
#         print(form.dept_code)
#         print(form.dept_code.data)
#         db.session.add(Employee(name=name, state=state, dept_code=dept_code))
#         db.session.commit()
#         return redirect("/phones")

#     else:

#         return render_template("employee_add_form.html", form=form)

@app.route("/snacks/new", methods=["GET", "POST"])
def add_snack():
    # print(request.form)
    form = AddSnackForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f'Created new snack: name is {name}, price is ${price}')
        return redirect("/phones")
    else: 
        return render_template("add_snack_form.html", form=form)
    
@app.route('/employees/new', methods=["GET", "POST"])
def add_employee():
    form = EmployeeForm()
    depts = db.sesison.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts
    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data
        emp = Employee(name"", state"", dept_code"")
        db.session.add(emp)
        db.session.commit()
        return redirect('/phones')
    else:
            return render_template('add_employee_form.html', form=form)

@app.route('/employees/<int: id>/edit', methods=["GET", "POST"])
def edit_employee(id):
    emp = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=emp)
    depts = db.sesison.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts

    if form.validate_on_submit():
        emp.name = form.name.data
        emp.state = form.data.sata
        emp.dept_code = form.dept_code.data
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template("edit_employee_form.html", form=form)

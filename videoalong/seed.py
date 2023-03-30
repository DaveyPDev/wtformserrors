""" Seed file to make sample data for db """

from models import Department, Employee, db
from app import app

#Create all tables

db.drop_all()
db.create_all()

d1 = Department(dept_code='mktg', dept_name='Marketing')
d2 = Department(dept_code='acct', dept_name='Accounting')
d3 = Department(dept_code='r&d', dept_name='Research and Development', phone='987-7878')
d4 = Department(dept_code='sales', dept_name='Sales', phone='225-6912')
d5 = Department(dept_code='it', dept_name='Information Technology', phone='888-4562')

river = Employee(name='River Bottom', state='NY', dept_code='mktg')
joaquin = Employee(name='Joaquin Phoenix', dept_code='acct')
summer = Employee(name='Summer Winter', state='OR', dept_code='mktg')
octavia = Employee(name='Octavia Spencer', dept_code='r&d')
larry = Employee(name='Larry David', state='NY' dept_code='r&d')
kurt = Employee(name='Kurt Cobain', state='WA', dept_code='it')
rain = Employee(name='Rain Phoenix', dept_code='it')


db.session.add_all([d1,d2,d3,d4,d5])

db.session.commit()

db.session.add_all([river, summer, joaquin, octavia, larry, kurt, rain])

db.session.commit()
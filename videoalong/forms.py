from flask_wtf import FlaskForm
from wtforms import SpringField, FloatField

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

class AddSnackForm(Flaskform):
    
    name = StringField("Snack Name")
    price = FloatField("Price in USD")
    # quantity = FloatField("Amount of Snack")

class NewEmployeeForm(FlaskForm):
    name = StringField('Employee Name')
    state = StringField('State')
    dept_code = StringField('Deptarment Code')

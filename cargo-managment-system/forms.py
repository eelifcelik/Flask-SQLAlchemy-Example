from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('You cannot leave this field blank.')


class addDepartment(Form):
    location = TextAreaField('Location', validators = [DataRequired()])
    dep_name = TextField('Department Name', validators = [DataRequired()])
    dep_num = IntegerField('Department Number', validators = [DataRequired()])
    region = TextField('Region', validators = [DataRequired()])


class addEmployee(Form):
    name = TextField('Name', validators = [DataRequired(), Length(min =3, max=10)])
    surname = TextField('Surname', validators = [DataRequired()])
    ssn = TextField('Social Security Number', validators = [DataRequired(), Length(11)])
    phone = TextField('Phone', validators = [Length(min=10, max=11)])
    employee_department = TextField('Employee Department', validators = [DataRequired()])


class addCargo(Form):
    cargo_id = IntegerField('Cargo ID', validators = [DataRequired()])
    weight = FloatField('Weight')
    shipper = TextAreaField('Shipper', validators = [DataRequired(),Length(min =3, max=10) ])
    customer_name = TextAreaField('Customer Name', validators = [DataRequired(), Length(min =3, max=10)])
    customer_surname = TextAreaField('Customer Surname', validators = [DataRequired(),Length(min =3, max=10)])
    adress = TextAreaField('Adress', validators = [DataRequired()])
    customer_phone = TextField('Customer Phone', validators = [DataRequired(),Length(min=10, max=11) ])
    cargo_department = TextField('Cargo Department', validators = [DataRequired()])


class addDeliveryCar(Form):

    model = TextAreaField('Car Model', validators = [DataRequired()]) 
    licence_id = TextAreaField('Car Licanse ID', validators = [DataRequired()])
    deliverycar_dep = TextField('Car Department', validators = [DataRequired()])
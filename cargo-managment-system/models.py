from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import app

db = SQLAlchemy(app)

class Employee(db.Model):
    name = db.Column(db.String(20),nullable=False)
    surname = db.Column(db.String(20),nullable=False)
    ssn = db.Column(db.String(11), primary_key=True)
    phone = db.Column(db.String(10), unique=True)

    employee_department = db.Column(db.Integer, db.ForeignKey('department.dep_num'))

    def __init__(self, name, surname, ssn, phone, employee_department):
        self.name = name
        self.surname = surname
        self.ssn = ssn
        self.phone = phone
        self.employee_department = employee_department


class Department(db.Model):
    location = db.Column(db.String(20))
    dep_name = db.Column(db.String(20),nullable=False)
    dep_num = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(20),nullable=False)

    cargos = db.relationship('Cargo', backref='has')
    delivery_cars = db.relationship('DeliveryCar', backref='has')
    employees = db.relationship('Employee', backref='works')

    def __init__(self, location, dep_name, dep_num, region):
        self.location = location
        self.dep_name = dep_name
        self.dep_num = dep_num
        self.region = region
    

class Cargo(db.Model):
    cargo_id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    shipper = db.Column(db.String(30))
    customer_name = db.Column(db.String(20))
    customer_surname = db.Column(db.String(20))
    adress = db.Column(db.String(30))
    customer_phone = db.Column(db.String(10))

    cargo_department = db.Column(db.Integer, db.ForeignKey('department.dep_num'))


    def __init__(self, cargo_id, weight, shipper, customer_name, customer_surname, adress, customer_phone, cargo_department):
        self.cargo_id = cargo_id
        self.weight = weight
        self.shipper = shipper
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.adress = adress
        self.customer_phone = customer_phone
        self.cargo_department = cargo_department
    

class DeliveryCar(db.Model):
    model = db.Column(db.String(20))
    licence_id = db.Column(db.String(8),primary_key=True)
    
    deliverycar_dep = db.Column(db.Integer, db.ForeignKey('department.dep_num'))

    def __init__(self, model, licence_id, deliverycar_dep):
        self.model = model
        self.licence_id = licence_id
        self.deliverycar_dep = deliverycar_dep
    
  
db.create_all()
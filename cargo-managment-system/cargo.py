from flask import Flask,render_template,redirect,url_for,request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import Employee, Department, Cargo, DeliveryCar, db
from forms import addCargo, addDeliveryCar,addEmployee,addDepartment
from __init__ import app

@app.route('/')
def index():
    return render_template('index.html')

"""
@app.route('/about/')
def about():
    return render_template('about.html')
"""

@app.route('/about/whoweare')
def whoweare():
    return render_template('whoweare.html')

@app.route('/employee/add', methods = ['GET', 'POST'])
def addemployees():
    form = addEmployee(request.form)
    if request.method == 'POST' and form.validate:
       
        name = form.name.data
        surname = form.surname.data
        ssn =  form.ssn.data
        phone = form.phone.data
        employee_department = form.employee_department.data

        emp = Employee(name=name,surname=surname,ssn=ssn,phone=phone,employee_department=employee_department)
        db.session.add(emp)
        db.session.commit()
        flash("Employee added succesfully.")

        return redirect(url_for("allemployees"))
     
    return render_template('addemployee.html', form = form)

@app.route('/employee/all')
def allemployees():
    all_emp = Employee.query.all()   
    return render_template('allemployees.html',employees = all_emp)


@app.route('/employee/delete/<ssn>/', methods = ['GET', 'POST'])
def EmployeeDelete(ssn):
    my_data = Employee.query.get(ssn)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Succesfully")

    return redirect(url_for('allemployees'))

@app.route('/employee/update', methods = ['GET', 'POST'])
def EmployeeUpdate():

    if request.method == 'POST':
        emp = Employee.query.get(request.form.get('ssn'))
        
        emp.name = request.form['name']
        emp.surname = request.form['surname']
        emp.phone = request.form['phone']
        emp.employee_department = request.form['employee_department']
        
        db.session.commit()
        flash("Employee Updated Succesfully")

        return redirect(url_for('allemployees'))

@app.route('/delivery/add', methods = ['GET', 'POST'])
def adddeliverycars():
    form = addDeliveryCar(request.form)
    if request.method == 'POST' and form.validate:
       
        model = form.model.data
        licence_id = form.licence_id.data
        deliverycar_dep = form.deliverycar_dep.data

        car = DeliveryCar(model= model, licence_id=licence_id, deliverycar_dep=deliverycar_dep)
        db.session.add(car)
        db.session.commit()
        flash("Delivery Car added succesfully.")

        return redirect(url_for("alldelivery"))

    return render_template('adddelivery.html', form = form)

@app.route('/delivery/all')
def alldelivery():
    all_deliverycars = DeliveryCar.query.all()
    return render_template('alldelivery.html', deliverycars = all_deliverycars) 

@app.route('/delivery/update', methods = ['GET', 'POST'])
def DeliveryCarUpdate():

    if request.method == 'POST':
        car = DeliveryCar.query.get(request.form.get('licence_id'))
        
        car.model = request.form['model']
        car.deliverycar_dep = request.form['deliverycar_dep']
        
        db.session.commit()
        flash("Delivery Car Updated Succesfully")

        return redirect(url_for('alldelivery'))

@app.route('/delivery/delete/<licence_id>/', methods = ['GET', 'POST'])
def DeliveryCarDelete(licence_id):
    my_data = DeliveryCar.query.get(licence_id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Delivery Car Deleted Succesfully")

    return redirect(url_for('alldelivery'))

@app.route('/departments/add', methods = ['GET', 'POST'])
def addDepartments():
    form = addDepartment(request.form)
    if request.method == 'POST' and form.validate:
       
        location = form.location.data
        dep_name = form.dep_name.data
        dep_num = form.dep_num.data
        region =  form.region.data
        
        dep = Department(location = location, dep_name= dep_name, dep_num=dep_num, region=region)
        db.session.add(dep)
        db.session.commit()

        return redirect(url_for("allDepartments"))

    return render_template('adddepartment.html', form = form)

@app.route('/departments/all')
def allDepartments():
    all_departments = Department.query.all()
    return render_template('allDepartments.html', departments = all_departments)
    
@app.route('/departments/update', methods = ['GET', 'POST'])
def DepartmentUpdate():

    if request.method == 'POST':
        dep = Department.query.get(request.form.get('dep_num'))
        
        dep.location = request.form['location']
        dep.dep_name = request.form['dep_name']
        dep.region = request.form['region']

        db.session.commit()
        flash("Department Updated Succesfully")

        return redirect(url_for('allDepartments'))

@app.route('/departments/delete/<dep_num>/', methods = ['GET', 'POST'])
def DepartmentDelete(dep_num):
    my_data = Department.query.get(dep_num)
    db.session.delete(my_data)
    db.session.commit()
    flash("Department Deleted Succesfully")

    return redirect(url_for('allDepartments'))


@app.route('/cargos/add', methods = ['GET', 'POST'])
def cargos():
    form = addCargo(request.form)
    if request.method == 'POST' and form.validate:
       
        cargo_id = form.cargo_id.data
        weight = form.weight.data
        shipper = form.shipper.data
        customer_name =  form.customer_name.data
        customer_surname = form.customer_surname.data
        adress = form.adress.data
        customer_phone = form.customer_phone.data
        cargo_department = form.cargo_department.data 

        cargo = Cargo(cargo_id=cargo_id, weight=weight, shipper=shipper, customer_name=customer_name, customer_surname=customer_surname,adress=adress,customer_phone=customer_phone,cargo_department=cargo_department)
        db.session.add(cargo)
        db.session.commit()

        return redirect(url_for("allcargos"))

     
    return render_template('addcargos.html', form = form)

@app.route('/cargos/all')
def allcargos():
    all_cargos = Cargo.query.all()
    return render_template('allcargos.html', cargos = all_cargos)

    
@app.route('/cargos/update', methods = ['GET', 'POST'])
def CargoUpdate():

    if request.method == 'POST':
        cargo = Cargo.query.get(request.form.get('cargo_id'))
        
        cargo.weight = request.form['weight']
        cargo.shipper = request.form['shipper']
        cargo.customer_name = request.form['customer_name']
        cargo.customer_surname = request.form['customer_surname']
        cargo.adress = request.form['adress']
        cargo.customer_phone = request.form['customer_phone']
        cargo.cargo_department = request.form['cargo_department']

        db.session.commit()
        flash("Cargo Updated Succesfully")

        return redirect(url_for('allcargos'))

@app.route('/cargos/delete/<cargo_id>/', methods = ['GET', 'POST'])
def CargoDelete(cargo_id):
    my_cargo = Cargo.query.get(cargo_id)
    db.session.delete(my_cargo)
    db.session.commit()
    flash("Cargo Deleted Succesfully")

    return redirect(url_for('allcargos'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.Booking import Booking
from models.Customer import Customer
from models.Treatment import Treatment
from app import db

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route("/customers")
def customers():
	customers = Customer.query.all()
	return render_template("customers/index.html", customers = customers)

@customers_blueprint.route("/customers/<id>")
def show(id):
	customer = Customer.query.get(id)
	treatments = Treatment.query.join(Booking).filter(Booking.customer_id == id)
	bookings = Booking.query.filter(Booking.customer_id == id)
	return render_template("customers/show.html", customer=customer, treatments=treatments, bookings=bookings)

# NEW
# GET '/customers/new'
@customers_blueprint.route("/customers/new")
def new_booking():
	return render_template("customers/new.html")

# CREATE
# POST '/customers'
@customers_blueprint.route("/customers",  methods=['POST'])
def create_customer():
	name = request.form['name']
	customer = Customer(name=name)
	db.session.add(customer)
	db.session.commit()
	return redirect('/customers')


# DELETE
# DELETE '/customers/<id>/delete'
@customers_blueprint.route("/customers/<id>/delete", methods=['POST'])
def delete_customer(id):
	Booking.query.filter_by(customer_id = id).delete()
	Customer.query.filter_by(id = id).delete()
	db.session.commit()
	return redirect('/customers')

@customers_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
	customer = Customer.query.get(id)
	return render_template('customers/edit.html', customer=customer)

@customers_blueprint.route("/customers/<id>", methods=["POST"])
def update_customer(id):
	name = request.form['name']
	
	customer = Customer.query.get(id)
	customer.name = name

	db.session.commit()
	return redirect('/customers')
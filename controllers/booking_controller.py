from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.Booking import Booking
from models.Customer import Customer
from models.Treatment import Treatment
from app import db

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
	bookings = Booking.query.all()
	return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
	customers = Customer.query.all()
	treatments = Treatment.query.all()
	return render_template("bookings/new.html", customers = customers, treatments = treatments)

@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_booking():
	customer_id = request.form['customer_id']
	treatment_id = request.form['treatment_id']
	name = request.form['name']
	date = request.form['date']
	booking = Booking(customer_id = customer_id, treatment_id = treatment_id, name=name, date=date)
	db.session.add(booking)
	db.session.commit()
	return redirect('/bookings')

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
	Booking.query.filter_by(id = id).delete()
	db.session.commit()
	return redirect('/bookings')

@bookings_blueprint.route("/bookings/<id>")
def show(id):
	booking = Booking.query.get(id)
	treatment=Treatment.query.get(booking.treatment_id)
	customer=Customer.query.get(booking.customer_id)
	return render_template("/bookings/show.html", name=booking.name, treatment_name=treatment.name, customer_name=customer.name, date=booking.date, treatment_id=treatment.id, customer_id=customer.id, booking_id=booking.id)

@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
	booking = Booking.query.get(id)
	customers = Customer.query.all()
	treatments = Treatment.query.all()
	return render_template('bookings/edit.html', booking=booking, customers=customers, treatments=treatments)

@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
	name = request.form['name']
	date = request.form['date']
	customer_id = request.form['customer_id']
	treatment_id = request.form['treatment_id']
	
	booking = Booking.query.get(id)
	booking.name = name
	booking.date = date
	booking.customer_id = customer_id
	booking.treatment_id = treatment_id

	db.session.commit()
	return redirect('/bookings')
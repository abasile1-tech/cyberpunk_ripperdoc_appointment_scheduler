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

# NEW
# GET '/bookings/new'
@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    customers = Customer.query.all()
    treatments = Treatment.query.all()
    return render_template("bookings/new.html", customers = customers, treatments = treatments)

# CREATE
# POST '/bookings'
@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_booking():
    customer_id = request.form['customer_id']
    treatment_id = request.form['treatment_id']
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    booking = Booking(customer_id = customer_id, treatment_id = treatment_id, name=name, date=date, time=time)
    db.session.add(booking)
    db.session.commit()
    return redirect('/bookings')


# DELETE
# DELETE '/bookings/<id>/delete'
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    Booking.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/bookings')
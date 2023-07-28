from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.Booking import Booking
from models.Customer import Customer
from models.Treatment import Treatment

from app import db

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route("/treatments")
def treatments():
	treatments = Treatment.query.all()
	return render_template("treatments/index.html", treatments = treatments)

@treatments_blueprint.route("/treatments/<id>")
def show(id):
	treatment = Treatment.query.get(id)
	customers = Customer.query.join(Booking).filter(Booking.treatment_id == id)
	return render_template("treatments/show.html", treatment=treatment, customers=customers)

# NEW
# GET '/treatments/new'
@treatments_blueprint.route("/treatments/new")
def new_booking():
	return render_template("treatments/new.html")

# CREATE
# POST '/treatments'
@treatments_blueprint.route("/treatments",  methods=['POST'])
def create_treatment():
	name = request.form['name']
	duration = request.form['duration']
	treatment = Treatment(name=name, duration=duration)
	db.session.add(treatment)
	db.session.commit()
	return redirect('/treatments')


# DELETE
# DELETE '/treatments/<id>/delete'
@treatments_blueprint.route("/treatments/<id>/delete", methods=['POST'])
def delete_treatment(id):
	Treatment.query.filter_by(id = id).delete()
	db.session.commit()
	return redirect('/treatments')
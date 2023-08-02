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

@treatments_blueprint.route("/treatments/new")
def new_booking():
	return render_template("treatments/new.html")

@treatments_blueprint.route("/treatments",  methods=['POST'])
def create_treatment():
	name = request.form['name']
	duration = request.form['duration']
	treatment = Treatment(name=name, duration=duration)
	db.session.add(treatment)
	db.session.commit()
	return redirect('/treatments')

@treatments_blueprint.route("/treatments/<id>/delete", methods=['POST'])
def delete_treatment(id):
	Booking.query.filter_by(treatment_id = id).delete()
	Treatment.query.filter_by(id = id).delete()
	db.session.commit()
	return redirect('/treatments')

@treatments_blueprint.route("/treatments/<id>/edit")
def edit_treatment(id):
	treatment = Treatment.query.get(id)
	return render_template('treatments/edit.html', treatment=treatment)

@treatments_blueprint.route("/treatments/<id>", methods=["POST"])
def update_treatment(id):
	name = request.form['name']
	duration = request.form['duration']
	
	treatment = Treatment.query.get(id)
	treatment.name = name
	treatment.duration = duration

	db.session.commit()
	return redirect('/treatments')
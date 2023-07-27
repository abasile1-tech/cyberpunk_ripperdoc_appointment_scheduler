from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Treatment, Customer, Booking
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
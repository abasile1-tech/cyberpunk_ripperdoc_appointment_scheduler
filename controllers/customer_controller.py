from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Customer, Treatment, Booking

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route("/customers")
def customers():
    customers = Customer.query.all()
    return render_template("customers/index.html", customers = customers)

@customers_blueprint.route("/customers/<id>")
def show(id):
    customer = Customer.query.get(id)
    treatments = Treatment.query.join(Booking).filter(Booking.customer_id == id)
    return render_template("customers/show.html", customer=customer, treatments=treatments)
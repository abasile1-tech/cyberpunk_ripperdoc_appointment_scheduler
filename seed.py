from app import db
from models.Treatment import Treatment
from models.Customer import Customer
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
	customer1 = Customer(name="V")
	customer2 = Customer(name="Maine")
	customer3 = Customer(name="David Martinez")

	treatment1 = Treatment(name="Mantis Blades", duration=840)
	treatment2 = Treatment(name="Gorilla Arms", duration=720)
	treatment3 = Treatment(name="Sandevistan", duration=900)

	db.session.add(customer1)
	db.session.add(customer2)
	db.session.add(customer3)

	db.session.add(treatment1)
	db.session.add(treatment2)
	db.session.add(treatment3)

	db.session.commit()
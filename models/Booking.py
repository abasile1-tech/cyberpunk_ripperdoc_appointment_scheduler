from app import db

class Booking(db.Model):
	__tablename__ = "bookings"

	id = db.Column(db.Integer, primary_key=True) 
	customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
	treatment_id = db.Column(db.Integer, db.ForeignKey('treatments.id'))
	name = db.Column(db.String(64))
	date = db.Column(db.DateTime(False))

	def __repr__(self):
		return f"<Booking: {self.id}: {self.name}, {self.date}>"
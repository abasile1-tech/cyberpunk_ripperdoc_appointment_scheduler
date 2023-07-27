from app import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    bookings = db.relationship('Booking', backref='customer')

    def __repr__(self):
        return f"<Customer: {self.id}: {self.name}>"
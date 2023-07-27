from app import db

class Treatment(db.Model):
  __tablename__ = "treatments"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  duration = db.Column(db.Integer)
  bookings = db.relationship('Booking', backref='treatment')

  def __repr__(self):
    return f"<Treatment: {self.id}: {self.name}>"
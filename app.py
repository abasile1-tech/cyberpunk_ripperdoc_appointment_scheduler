from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{PASSWORD}@localhost:5432/cyberpunk_ripperdoc_appointment_scheduler"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from controllers.booking_controller import bookings_blueprint
from controllers.treatment_controller import treatments_blueprint
from controllers.customer_controller import customers_blueprint

app.register_blueprint(bookings_blueprint)
app.register_blueprint(treatments_blueprint)
app.register_blueprint(customers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
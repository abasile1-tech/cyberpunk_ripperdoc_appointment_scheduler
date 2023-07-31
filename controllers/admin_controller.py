from flask import Flask, render_template
from flask import Blueprint

admin_blueprint = Blueprint("admin", __name__)

@admin_blueprint.route("/admin-portal")
def admin_portal():
	return render_template("admin_portal.html")

@admin_blueprint.route("/customer-portal")
def customer_portal():
	return render_template("customer_portal.html")
from flask import render_template
from flask_login import login_required
from apps.app import app


@app.route("/dashboard")
# @login_required
def dashboard():
    print("dashboard working")
    return render_template("dashboard.html")

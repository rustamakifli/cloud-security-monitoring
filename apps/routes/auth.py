from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from apps.models.user import User
from apps.config import db,login_manager
from werkzeug.security import check_password_hash
from main import app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/login", methods=["GET", "POST"])
def login():
    print("test")
    # if request.method == "POST":
    #     email = request.form["email"]
    #     password = request.form["password"]
    #     user = User.query.filter_by(email=email).first()

    #     if user and user.check_password(password):
    #         login_user(user)
    #         flash("Login successful!", "success")
    #         return redirect(url_for("dashboard"))

    #     flash("Invalid credentials", "danger")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            flash("Email already in use", "warning")
            return redirect(url_for("auth.register"))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("auth.login"))

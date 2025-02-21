from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from apps.models.user import User
from apps.config import db, login_manager
from werkzeug.security import check_password_hash
from main import app
from apps.forms import LoginForm, RegisterForm  # Import the forms


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid credentials", "danger")

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(email=email).first():
            flash("Email already in use", "warning")
            return redirect(url_for("register"))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        print("User added to database")
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("login"))

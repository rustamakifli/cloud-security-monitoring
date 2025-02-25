from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[DataRequired()],render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=50)], render_kw={"placeholder": "Username"}
    )
    email = StringField("Email", validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, message="Password must be at least 6 characters long."),
        ],
        render_kw={"placeholder": "Passsword"}
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
        render_kw={"placeholder": "Confirm Password"}
    )
    submit = SubmitField("Register")

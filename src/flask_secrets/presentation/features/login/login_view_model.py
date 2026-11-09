"""@brief View model of the login page: the Flask-WTF form."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField


class LoginForm(FlaskForm):  # type: ignore[misc]
    """@brief The login form (lecture steps 2 and 3)."""

    email = StringField(label="Email")
    password = PasswordField(label="Password")
    submit = SubmitField(label="Log In")

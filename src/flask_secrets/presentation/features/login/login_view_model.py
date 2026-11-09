"""@brief View model of the login page: the Flask-WTF form."""

from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):  # type: ignore[misc]
    """@brief The login form with an email and a password field (lecture step 2)."""

    email = StringField("Email")
    password = StringField("Password")

"""@brief View model of the login page: the Flask-WTF form."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):  # type: ignore[misc]
    """@brief The login form (lecture steps 2 to 4)."""

    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

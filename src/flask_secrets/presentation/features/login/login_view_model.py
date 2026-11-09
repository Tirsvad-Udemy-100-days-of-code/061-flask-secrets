"""@brief View model of the login page: the Flask-WTF form."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from flask_secrets.constants import INPUT_SIZE, PASSWORD_MIN_LENGTH


class LoginForm(FlaskForm):  # type: ignore[misc]
    """@brief The login form (lecture steps 2 to 5 and 10)."""

    email = StringField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={"size": INPUT_SIZE},
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired(), Length(min=PASSWORD_MIN_LENGTH)],
        render_kw={"size": INPUT_SIZE},
    )
    submit = SubmitField(label="Log In")

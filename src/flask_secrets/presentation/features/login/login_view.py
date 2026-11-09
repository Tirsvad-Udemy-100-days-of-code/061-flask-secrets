"""@brief Routes of the login feature (the view side of the presentation layer)."""

from flask import Flask, render_template

from flask_secrets.constants import INPUT_SIZE
from flask_secrets.presentation.features.login.login_view_model import LoginForm


def home() -> str:
    """@brief Render the home page.

    @return The HTML of index.html.
    """
    return render_template("index.html")


def login() -> str:
    """@brief Render the login page with its Flask-WTF form (lecture step 2).

    @return The HTML of login.html.
    """
    form = LoginForm()
    return render_template("login.html", form=form, input_size=INPUT_SIZE)


def register_routes(app: Flask) -> None:
    """@brief Attach the routes of this feature to the application.

    @param app The Flask application to extend.
    """
    app.add_url_rule("/", endpoint="home", view_func=home)
    app.add_url_rule("/login", endpoint="login", view_func=login)

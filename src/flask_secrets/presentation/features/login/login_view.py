"""@brief Routes of the login feature (the view side of the presentation layer)."""

from flask import Flask, render_template

from flask_secrets.application.use_cases.authenticate_user import authenticate_user
from flask_secrets.presentation.features.login.login_view_model import LoginForm


def home() -> str:
    """@brief Render the home page.

    @return The HTML of index.html.
    """
    return render_template("index.html")


def login() -> str:
    """@brief Show the login form, then accept or deny a valid submit (step 6).

    @return login.html, or success.html or denied.html after a valid submit.
    """
    form = LoginForm()
    if form.validate_on_submit():
        if authenticate_user(form.email.data or "", form.password.data or ""):
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=form)


def register_routes(app: Flask) -> None:
    """@brief Attach the routes of this feature to the application.

    @param app The Flask application to extend.
    """
    app.add_url_rule("/", endpoint="home", view_func=home)
    app.add_url_rule(
        "/login", endpoint="login", view_func=login, methods=["GET", "POST"]
    )

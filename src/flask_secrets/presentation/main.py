"""@brief Entry point and composition root of the Flask Secrets site."""

import os

from flask import Flask
from flask_bootstrap import Bootstrap5

from flask_secrets.constants import (
    BOOTSTRAP_SERVE_LOCAL,
    DEFAULT_SECRET_KEY,
    SECRET_KEY_ENV,
)
from flask_secrets.presentation.features.login.login_view import register_routes


def create_app() -> Flask:
    """@brief Build the Flask application.

    @return The configured application.
    """
    app = Flask(__name__)
    app.secret_key = os.environ.get(SECRET_KEY_ENV, DEFAULT_SECRET_KEY)
    app.config["BOOTSTRAP_SERVE_LOCAL"] = BOOTSTRAP_SERVE_LOCAL
    Bootstrap5(app)
    register_routes(app)
    return app


def main() -> None:
    """@brief Start the development server."""
    create_app().run(debug=True)


if __name__ == "__main__":
    main()

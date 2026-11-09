"""@brief Entry point and composition root of the Flask Secrets site."""

from flask import Flask

from flask_secrets.presentation.features.login.login_view import register_routes


def create_app() -> Flask:
    """@brief Build the Flask application.

    @return The configured application.
    """
    app = Flask(__name__)
    register_routes(app)
    return app


def main() -> None:
    """@brief Start the development server."""
    create_app().run(debug=True)


if __name__ == "__main__":
    main()

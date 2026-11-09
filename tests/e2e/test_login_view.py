"""@brief End-to-end tests of the login feature through the Flask test client."""

import pytest
from flask.testing import FlaskClient

from flask_secrets.presentation.main import create_app


@pytest.fixture
def client() -> FlaskClient:
    """@brief A test client for a fresh application."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_home_page_answers_ok(client: FlaskClient) -> None:
    """@brief The home page is served."""
    assert client.get("/").status_code == 200


def test_login_route_renders_login_page(client: FlaskClient) -> None:
    """@brief GET /login answers 200 and shows the login heading."""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"<h1>Login</h1>" in response.data

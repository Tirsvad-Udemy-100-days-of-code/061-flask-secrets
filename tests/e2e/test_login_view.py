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


def test_login_form_has_csrf_token(client: FlaskClient) -> None:
    """@brief The form carries a hidden CSRF token."""
    response = client.get("/login")
    assert b'name="csrf_token"' in response.data


def test_login_form_inputs_have_size_30(client: FlaskClient) -> None:
    """@brief Email and password inputs are 30 characters wide."""
    html = client.get("/login").get_data(as_text=True)
    assert html.count('size="30"') == 2


def test_password_input_hides_typed_text(client: FlaskClient) -> None:
    """@brief The password field is rendered as a password input."""
    html = client.get("/login").get_data(as_text=True)
    assert 'type="password"' in html


def test_form_action_is_built_with_url_for(client: FlaskClient) -> None:
    """@brief The form posts to the URL of the login endpoint."""
    html = client.get("/login").get_data(as_text=True)
    assert '<form action="/login" method="post" novalidate>' in html


def test_submit_button_uses_its_label(client: FlaskClient) -> None:
    """@brief The SubmitField renders a button labelled Log In."""
    html = client.get("/login").get_data(as_text=True)
    assert 'type="submit" value="Log In"' in html


def test_form_turns_browser_validation_off(client: FlaskClient) -> None:
    """@brief The form carries the novalidate attribute."""
    assert "novalidate" in client.get("/login").get_data(as_text=True)


def test_empty_submit_shows_required_errors(client: FlaskClient) -> None:
    """@brief Posting empty fields shows a required-field error for each field."""
    client.application.config["WTF_CSRF_ENABLED"] = False
    html = client.post("/login", data={}).get_data(as_text=True)
    assert html.count("This field is required.") == 2

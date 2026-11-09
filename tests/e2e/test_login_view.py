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


def test_email_without_at_sign_is_rejected(client: FlaskClient) -> None:
    """@brief An email without @ shows the invalid email error."""
    client.application.config["WTF_CSRF_ENABLED"] = False
    data = {"email": "admin.email.com", "password": "12345678"}
    html = client.post("/login", data=data).get_data(as_text=True)
    assert "Invalid email address." in html


def test_short_password_is_rejected(client: FlaskClient) -> None:
    """@brief A password of 4 characters shows the minimum length error."""
    client.application.config["WTF_CSRF_ENABLED"] = False
    data = {"email": "admin@email.com", "password": "1234"}
    html = client.post("/login", data=data).get_data(as_text=True)
    assert "Field must be at least 8 characters long." in html


def test_valid_input_shows_no_validation_error(client: FlaskClient) -> None:
    """@brief A valid email and an 8 character password show no error."""
    client.application.config["WTF_CSRF_ENABLED"] = False
    data = {"email": "admin@email.com", "password": "12345678"}
    html = client.post("/login", data=data).get_data(as_text=True)
    assert "color: red" not in html


def test_demo_account_sees_the_secret_page(client: FlaskClient) -> None:
    """@brief The right credentials show the success page."""
    client.application.config["WTF_CSRF_ENABLED"] = False
    data = {"email": "admin@email.com", "password": "12345678"}
    html = client.post("/login", data=data).get_data(as_text=True)
    assert "<h1>Top Secret</h1>" in html


def test_other_credentials_see_access_denied(client: FlaskClient) -> None:
    """@brief Valid but wrong credentials show the denied page."""
    client.application.config["WTF_CSRF_ENABLED"] = False
    data = {"email": "user@email.com", "password": "87654321"}
    html = client.post("/login", data=data).get_data(as_text=True)
    assert "<h1>Access Denied</h1>" in html

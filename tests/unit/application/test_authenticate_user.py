"""@brief Unit tests of the authenticate_user use case."""

from flask_secrets.application.use_cases.authenticate_user import authenticate_user


def test_accepts_the_demo_account() -> None:
    """@brief The lecture account is accepted."""
    assert authenticate_user("admin@email.com", "12345678")


def test_refuses_other_credentials() -> None:
    """@brief Any other credentials are refused."""
    assert not authenticate_user("someone@email.com", "password1")

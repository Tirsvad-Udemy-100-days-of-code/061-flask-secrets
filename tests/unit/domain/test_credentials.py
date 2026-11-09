"""@brief Unit tests of the Credentials value object."""

from flask_secrets.domain.credentials import Credentials


def test_demo_account_is_admin() -> None:
    """@brief The lecture account is accepted."""
    assert Credentials("admin@email.com", "12345678").is_admin()


def test_wrong_password_is_not_admin() -> None:
    """@brief A wrong password is refused."""
    assert not Credentials("admin@email.com", "87654321").is_admin()


def test_wrong_email_is_not_admin() -> None:
    """@brief A wrong email is refused."""
    assert not Credentials("user@email.com", "12345678").is_admin()

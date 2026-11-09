"""@brief Use case: decide whether a login attempt is accepted."""

from flask_secrets.domain.credentials import Credentials


def authenticate_user(email: str, password: str) -> bool:
    """@brief Check a login attempt against the demo account.

    @param email The email the user typed.
    @param password The password the user typed.
    @return True when the attempt is accepted.
    """
    return Credentials(email=email, password=password).is_admin()

"""@brief The credentials of a login attempt and the rule that checks them."""

import hmac
from dataclasses import dataclass

from flask_secrets.constants import ADMIN_EMAIL, ADMIN_PASSWORD


@dataclass(frozen=True)
class Credentials:
    """@brief An email and a password offered by a user."""

    email: str
    password: str

    def is_admin(self) -> bool:
        """@brief Tell whether these are the credentials of the demo account.

        The values are compared in constant time, so the answer does not leak
        how much of them matched.

        @return True when both the email and the password match.
        """
        email_matches = hmac.compare_digest(self.email.encode(), ADMIN_EMAIL.encode())
        password_matches = hmac.compare_digest(
            self.password.encode(), ADMIN_PASSWORD.encode()
        )
        return email_matches and password_matches

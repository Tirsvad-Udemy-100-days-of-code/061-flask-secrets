"""@brief Guards the lecture values kept in constants.py."""

from flask_secrets import constants


def test_lecture_values() -> None:
    """@brief Lecture demands size 30, minimum length 8 and the demo account."""
    assert constants.INPUT_SIZE == 30
    assert constants.PASSWORD_MIN_LENGTH == 8
    assert constants.ADMIN_EMAIL == "admin@email.com"
    assert constants.ADMIN_PASSWORD == "12345678"

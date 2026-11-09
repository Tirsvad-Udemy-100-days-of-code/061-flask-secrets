"""@brief Every constant of the project lives in this module."""

## @brief Name shown in page titles.
APP_NAME: str = "Flask Secrets"

## @brief Minimum number of characters of a password (lecture step 5).
PASSWORD_MIN_LENGTH: int = 8

## @brief Width of the email and password inputs (lecture step 2).
INPUT_SIZE: int = 30

## @brief Key that signs the CSRF token.
#  Lecture value; override it with the SECRET_KEY environment variable.
DEFAULT_SECRET_KEY: str = "lecture-secret-key-change-me"

## @brief Name of the environment variable that overrides the secret key.
SECRET_KEY_ENV: str = "SECRET_KEY"

## @brief The one demo account of the lecture. Not a real credential.
ADMIN_EMAIL: str = "admin@email.com"

## @brief Password of the demo account. Not a real credential.
ADMIN_PASSWORD: str = "12345678"

## @brief Serve the Bootstrap files from this site instead of a CDN.
BOOTSTRAP_SERVE_LOCAL: bool = True

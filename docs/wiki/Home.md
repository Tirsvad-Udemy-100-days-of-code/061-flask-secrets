**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Flask Secrets: Day 61, advanced forms

This wiki explains what each lecture step of Day 61 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" taught us. We built a Flask site with a login form that only shows a secret page to the right user.

## Run it

Create a local `.venv`, upgrade pip, install the project and start it (the full instructions are in the [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m flask_secrets.presentation.main
```

The account `admin@email.com` with the password `12345678` is a lecture demo, not a real credential.

## The ten steps

1. [Step 1: The login route](Step-01-Login-Route)
2. [Step 2: A login form with Flask-WTF](Step-02-Flask-WTF-Form)
3. [Step 3: Five code improvements](Step-03-Code-Improvements)
4. [Step 4: Required fields and novalidate](Step-04-Required-Validation)
5. [Step 5: Email and length validation](Step-05-Email-And-Length-Validation)
6. [Step 6: Check the credentials](Step-06-Check-Credentials)
7. [Step 7: Template inheritance](Step-07-Template-Inheritance)
8. [Step 8: Super blocks](Step-08-Super-Blocks)
9. [Step 9: Bootstrap-Flask](Step-09-Bootstrap-Flask)
10. [Step 10: render_form](Step-10-Render-Form)

## What we gained overall

- Forms as Python classes with Flask-WTF, including CSRF protection.
- Ready-made validators and clear error messages.
- Template inheritance and Bootstrap-Flask for a consistent design.
- Business rules kept apart from Flask and covered by pytest tests.

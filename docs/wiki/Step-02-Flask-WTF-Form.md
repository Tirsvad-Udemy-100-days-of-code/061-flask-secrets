**English** · [Dansk](Step-02-Flask-WTF-Form-da) · [Bahasa Malaysia](Step-02-Flask-WTF-Form-ms)

# Step 2: A login form with Flask-WTF

## What the lecture asked

Build a form with an email and a password field (both `StringField`, size 30) and CSRF protection, without writing `<label>` or `<input>` by hand.

## What we built

`LoginForm` inherits from `FlaskForm`. The template prints `form.csrf_token` and each field. The app has a secret key that signs the token.

```
class LoginForm(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")
```

## What it looks like

![Step 2: A login form with Flask-WTF](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-02-flask-wtf-form.png)

## What we gained

- A form is a Python class, and class inheritance gives it its behaviour.
- The CSRF token and the secret key stop other sites from posting in the name of a user.
- The template draws the fields from the form object, so the HTML stays short.

Previous step: [The login route](Step-01-Login-Route) · Next step: [Five code improvements](Step-03-Code-Improvements) · [Back to the overview](Home)

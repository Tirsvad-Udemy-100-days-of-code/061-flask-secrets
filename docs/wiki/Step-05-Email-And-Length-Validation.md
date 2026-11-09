**English** · [Dansk](Step-05-Email-And-Length-Validation-da) · [Bahasa Malaysia](Step-05-Email-And-Length-Validation-ms)

# Step 5: Email and length validation

## What the lecture asked

The email must be a valid address and the password must have at least 8 characters.

## What we built

`Email()` and `Length(min=8)` were added. `Email()` needs the extra package `email-validator`. The number 8 lives in `constants.py`.

```
password = PasswordField(
    label="Password",
    validators=[DataRequired(), Length(min=PASSWORD_MIN_LENGTH)],
)
```

## What it looks like

![Step 5: Email and length validation](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-05-email-and-length-validation.png)

## What we gained

- Ready-made validators replace our own checks for emails and lengths.
- Some validators need an extra package, and the documentation says so.
- A constant in one module (`constants.py`) keeps a rule in one place.

Previous step: [Required fields and novalidate](Step-04-Required-Validation) · Next step: [Check the credentials](Step-06-Check-Credentials) · [Back to the overview](Home)

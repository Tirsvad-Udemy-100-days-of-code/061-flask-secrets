**English** · [Dansk](Step-03-Code-Improvements-da) · [Bahasa Malaysia](Step-03-Code-Improvements-ms)

# Step 3: Five code improvements

## What the lecture asked

Use `PasswordField`, name the `label` argument, build the action with `url_for`, lay out the fields with a table and use `SubmitField`.

## What we built

The password field hides what is typed, the button comes from the form and the action follows the route name.

```
email = StringField(label="Email")
password = PasswordField(label="Password")
submit = SubmitField(label="Log In")
```

## What it looks like

![Step 3: Five code improvements](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-03-code-improvements.png)

## What we gained

- Choosing the right field type improves both safety and use.
- A URL built with `url_for` keeps working when the route path changes.
- Plain HTML around WTForms fields gives full control of the layout.

Previous step: [A login form with Flask-WTF](Step-02-Flask-WTF-Form) · Next step: [Required fields and novalidate](Step-04-Required-Validation) · [Back to the overview](Home)

**English** · [Dansk](Step-06-Check-Credentials-da) · [Bahasa Malaysia](Step-06-Check-Credentials-ms)

# Step 6: Check the credentials

## What the lecture asked

If the submitted form is valid and the email is `admin@email.com` and the password `12345678`, show `success.html`; otherwise show `denied.html`.

## What we built

The rule is in the `domain` layer (`Credentials.is_admin`), the use case `authenticate_user` is in the `application` layer and the route only calls it. The account is a lecture demo, not a real credential.

```
if form.validate_on_submit():
    if authenticate_user(form.email.data, form.password.data):
        return render_template("success.html")
    return render_template("denied.html")
```

## What it looks like

![Step 6: Check the credentials](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-06-success.png)

![Step 6: Check the credentials](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-06-denied.png)

## What we gained

- `form.<field>.data` gives the value the user typed.
- The result of `validate_on_submit()` tells a submit from a plain page view.
- A business rule can live outside Flask and be tested alone; the comparison runs in constant time.

Previous step: [Email and length validation](Step-05-Email-And-Length-Validation) · Next step: [Template inheritance](Step-07-Template-Inheritance) · [Back to the overview](Home)

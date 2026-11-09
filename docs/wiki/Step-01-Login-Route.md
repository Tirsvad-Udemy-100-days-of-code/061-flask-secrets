**English** · [Dansk](Step-01-Login-Route-da) · [Bahasa Malaysia](Step-01-Login-Route-ms)

# Step 1: The login route

## What the lecture asked

Create a `login` route that renders `login.html`.

## What we built

The function `login` renders the template and is registered at `/login`. The home page `home` is registered at `/`.

```
def login() -> str:
    return render_template("login.html")

app.add_url_rule("/login", endpoint="login", view_func=login)
```

## What it looks like

![Step 1: The login route](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-01-login-route.png)

## What we gained

- A Flask route connects a URL to a Python function.
- `render_template` looks for HTML files in the `templates` folder.
- Keeping routes in a `presentation` package separates the web part from the rules.

Next step: [A login form with Flask-WTF](Step-02-Flask-WTF-Form) · [Back to the overview](Home)

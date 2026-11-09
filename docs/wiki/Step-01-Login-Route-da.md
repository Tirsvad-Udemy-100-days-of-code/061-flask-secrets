[English](Step-01-Login-Route) · **Dansk** · [Bahasa Malaysia](Step-01-Login-Route-ms)

# Trin 1: Login-ruten

## Hvad lektionen bad om

Lav en rute `login`, der viser `login.html`.

## Hvad vi byggede

Funktionen `login` viser skabelonen og er registreret på `/login`. Forsiden `home` er registreret på `/`.

```
def login() -> str:
    return render_template("login.html")

app.add_url_rule("/login", endpoint="login", view_func=login)
```

## Sådan ser det ud

![Trin 1: Login-ruten](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-01-login-route.png)

## Hvad vi lærte

- En Flask-rute forbinder en URL med en Python-funktion.
- `render_template` leder efter HTML-filer i mappen `templates`.
- Når ruterne ligger i en `presentation`-pakke, holdes webdelen adskilt fra reglerne.

Næste trin: [En login-formular med Flask-WTF](Step-02-Flask-WTF-Form-da) · [Tilbage til oversigten](Home-da)

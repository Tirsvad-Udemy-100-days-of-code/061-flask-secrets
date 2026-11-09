[English](Step-02-Flask-WTF-Form) · **Dansk** · [Bahasa Malaysia](Step-02-Flask-WTF-Form-ms)

# Trin 2: En login-formular med Flask-WTF

## Hvad lektionen bad om

Byg en formular med felterne e-mail og adgangskode (begge `StringField`, størrelse 30) og CSRF-beskyttelse, uden at skrive `<label>` eller `<input>` i hånden.

## Hvad vi byggede

`LoginForm` arver fra `FlaskForm`. Skabelonen skriver `form.csrf_token` og hvert felt. Appen har en hemmelig nøgle, der signerer tokenet.

```
class LoginForm(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")
```

## Sådan ser det ud

![Trin 2: En login-formular med Flask-WTF](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-02-flask-wtf-form.png)

## Hvad vi lærte

- En formular er en Python-klasse, og arv giver den sin adfærd.
- CSRF-tokenet og den hemmelige nøgle forhindrer andre sider i at sende data i en brugers navn.
- Skabelonen tegner felterne ud fra formularobjektet, så HTML-koden forbliver kort.

Forrige trin: [Login-ruten](Step-01-Login-Route-da) · Næste trin: [Fem kodeforbedringer](Step-03-Code-Improvements-da) · [Tilbage til oversigten](Home-da)

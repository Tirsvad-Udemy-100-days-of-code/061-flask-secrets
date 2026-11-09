[English](Step-03-Code-Improvements) · **Dansk** · [Bahasa Malaysia](Step-03-Code-Improvements-ms)

# Trin 3: Fem kodeforbedringer

## Hvad lektionen bad om

Brug `PasswordField`, navngiv argumentet `label`, byg formularens action med `url_for`, opstil felterne i en tabel og brug `SubmitField`.

## Hvad vi byggede

Adgangskodefeltet skjuler det, der skrives, knappen kommer fra formularen, og action følger rutens navn.

```
email = StringField(label="Email")
password = PasswordField(label="Password")
submit = SubmitField(label="Log In")
```

## Sådan ser det ud

![Trin 3: Fem kodeforbedringer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-03-code-improvements.png)

## Hvad vi lærte

- Den rette felttype forbedrer både sikkerhed og brug.
- En URL bygget med `url_for` virker stadig, når rutens sti ændres.
- Almindelig HTML omkring WTForms-felter giver fuld kontrol over layoutet.

Forrige trin: [En login-formular med Flask-WTF](Step-02-Flask-WTF-Form-da) · Næste trin: [Påkrævede felter og novalidate](Step-04-Required-Validation-da) · [Tilbage til oversigten](Home-da)

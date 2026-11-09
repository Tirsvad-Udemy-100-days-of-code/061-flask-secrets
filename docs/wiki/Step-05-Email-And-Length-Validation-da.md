[English](Step-05-Email-And-Length-Validation) · **Dansk** · [Bahasa Malaysia](Step-05-Email-And-Length-Validation-ms)

# Trin 5: Validering af e-mail og længde

## Hvad lektionen bad om

E-mailen skal være en gyldig adresse, og adgangskoden skal have mindst 8 tegn.

## Hvad vi byggede

`Email()` og `Length(min=8)` blev tilføjet. `Email()` kræver pakken `email-validator`. Tallet 8 står i `constants.py`.

```
password = PasswordField(
    label="Password",
    validators=[DataRequired(), Length(min=PASSWORD_MIN_LENGTH)],
)
```

## Sådan ser det ud

![Trin 5: Validering af e-mail og længde](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-05-email-and-length-validation.png)

## Hvad vi lærte

- Færdige validatorer erstatter vores egne kontroller af e-mail og længde.
- Nogle validatorer kræver en ekstra pakke, og dokumentationen fortæller det.
- En konstant i ét modul (`constants.py`) holder en regel ét sted.

Forrige trin: [Påkrævede felter og novalidate](Step-04-Required-Validation-da) · Næste trin: [Kontrollér loginoplysningerne](Step-06-Check-Credentials-da) · [Tilbage til oversigten](Home-da)

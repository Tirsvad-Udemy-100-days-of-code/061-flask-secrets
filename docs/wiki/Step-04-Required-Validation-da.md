[English](Step-04-Required-Validation) · **Dansk** · [Bahasa Malaysia](Step-04-Required-Validation-ms)

# Trin 4: Påkrævede felter og novalidate

## Hvad lektionen bad om

Tilføj `DataRequired`, vis `form.<felt>.errors`, tag imod POST med `validate_on_submit()` og slå browserens validering fra med `novalidate`.

## Hvad vi byggede

Begge felter har en `DataRequired`-validator. Ruten accepterer GET og POST. Fejl vises med rødt ved feltet.

```
email = StringField(label="Email", validators=[DataRequired()])

if form.validate_on_submit():
    ...
```

## Sådan ser det ud

![Trin 4: Påkrævede felter og novalidate](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-04-required-validation.png)

## Hvad vi lærte

- Validatorer kontrollerer input uden vores egen kode.
- `validate_on_submit()` er falsk ved en GET-forespørgsel og når en validator fejler.
- `novalidate` giver alle browsere de samme beskeder, så vi kan teste dem.

Forrige trin: [Fem kodeforbedringer](Step-03-Code-Improvements-da) · Næste trin: [Validering af e-mail og længde](Step-05-Email-And-Length-Validation-da) · [Tilbage til oversigten](Home-da)

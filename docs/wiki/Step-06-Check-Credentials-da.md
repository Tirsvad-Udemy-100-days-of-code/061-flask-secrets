[English](Step-06-Check-Credentials) · **Dansk** · [Bahasa Malaysia](Step-06-Check-Credentials-ms)

# Trin 6: Kontrollér loginoplysningerne

## Hvad lektionen bad om

Hvis den indsendte formular er gyldig, og e-mailen er `admin@email.com` og adgangskoden `12345678`, vis `success.html`; ellers vis `denied.html`.

## Hvad vi byggede

Reglen ligger i `domain`-laget (`Credentials.is_admin`), use casen `authenticate_user` ligger i `application`-laget, og ruten kalder den kun. Kontoen er en demo fra lektionen, ikke en rigtig adgangskode.

```
if form.validate_on_submit():
    if authenticate_user(form.email.data, form.password.data):
        return render_template("success.html")
    return render_template("denied.html")
```

## Sådan ser det ud

![Trin 6: Kontrollér loginoplysningerne](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-06-success.png)

![Trin 6: Kontrollér loginoplysningerne](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-06-denied.png)

## Hvad vi lærte

- `form.<felt>.data` giver den værdi, brugeren skrev.
- Resultatet af `validate_on_submit()` skelner mellem en indsendelse og en almindelig sidevisning.
- En forretningsregel kan ligge uden for Flask og testes alene; sammenligningen tager konstant tid.

Forrige trin: [Validering af e-mail og længde](Step-05-Email-And-Length-Validation-da) · Næste trin: [Skabelonarv](Step-07-Template-Inheritance-da) · [Tilbage til oversigten](Home-da)

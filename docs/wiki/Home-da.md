[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Flask Secrets: Dag 61, avancerede formularer

Denne wiki forklarer, hvad hvert trin i dag 61 af Udemy-kurset "100 Days of Code: The Complete Python Pro Bootcamp" lærte os. Vi byggede et Flask-site med en login-formular, der kun viser en hemmelig side til den rette bruger.

## Kør det

Opret et lokalt `.venv`, opgradér pip, installér projektet og start det (den fulde vejledning står i [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m flask_secrets.presentation.main
```

Kontoen `admin@email.com` med adgangskoden `12345678` er en demo fra lektionen, ikke en rigtig adgangskode.

## De ti trin

1. [Trin 1: Login-ruten](Step-01-Login-Route-da)
2. [Trin 2: En login-formular med Flask-WTF](Step-02-Flask-WTF-Form-da)
3. [Trin 3: Fem kodeforbedringer](Step-03-Code-Improvements-da)
4. [Trin 4: Påkrævede felter og novalidate](Step-04-Required-Validation-da)
5. [Trin 5: Validering af e-mail og længde](Step-05-Email-And-Length-Validation-da)
6. [Trin 6: Kontrollér loginoplysningerne](Step-06-Check-Credentials-da)
7. [Trin 7: Skabelonarv](Step-07-Template-Inheritance-da)
8. [Trin 8: Super-blokke](Step-08-Super-Blocks-da)
9. [Trin 9: Bootstrap-Flask](Step-09-Bootstrap-Flask-da)
10. [Trin 10: render_form](Step-10-Render-Form-da)

## Hvad vi lærte samlet set

- Formularer som Python-klasser med Flask-WTF, inklusive CSRF-beskyttelse.
- Færdige validatorer og tydelige fejlbeskeder.
- Skabelonarv og Bootstrap-Flask for et ensartet design.
- Forretningsregler holdt adskilt fra Flask og dækket af pytest-tests.

[English](Step-10-Render-Form) · **Dansk** · [Bahasa Malaysia](Step-10-Render-Form-ms)

# Trin 10: render_form

## Hvad lektionen bad om

Erstat den håndskrevne formular med `render_form(form)` fra Bootstrap-Flask.

## Hvad vi byggede

Én linje tegner labels, felter, knap, CSRF-token og fejlbeskeder. Feltstørrelsen 30 bevares med `render_kw` i formularklassen.

```
{% from 'bootstrap5/form.html' import render_form %}
{{ render_form(form, action=url_for('login'), novalidate=True) }}
```

## Sådan ser det ud

![Trin 10: render_form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-10-render-form.png)

## Hvad vi lærte

- En makro kan erstatte snesevis af linjer HTML.
- Det hjælper at kende formularens indre, før man bruger genvejen, så en ødelagt formular kan fejlsøges.
- Feltindstillinger som størrelsen hører hjemme i formularklassen, hvor alle visere kan bruge dem.

Forrige trin: [Bootstrap-Flask](Step-09-Bootstrap-Flask-da) · [Tilbage til oversigten](Home-da)

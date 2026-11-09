[English](Step-07-Template-Inheritance) · **Dansk** · [Bahasa Malaysia](Step-07-Template-Inheritance-ms)

# Trin 7: Skabelonarv

## Hvad lektionen bad om

Lav `base.html` med blokke, og lad `success.html` og `denied.html` udvide den.

## Hvad vi byggede

`base.html` har en `title`-blok og en `content`-blok. Børnesiderne starter med `{% extends "base.html" %}` og udfylder blokkene.

```
{% extends "base.html" %}
{% block title %}Success{% endblock %}
{% block content %}
<h1>Top Secret</h1>
{% endblock %}
```

## Sådan ser det ud

![Trin 7: Skabelonarv](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-07-base-template.png)

## Hvad vi lærte

- Én forældreskabelon rummer den fælles sideramme, så den skrives én gang.
- `extends` passer til sider med samme design; `include` passer til små fælles stykker.
- En ændring af rammen rammer alle sider.

Forrige trin: [Kontrollér loginoplysningerne](Step-06-Check-Credentials-da) · Næste trin: [Super-blokke](Step-08-Super-Blocks-da) · [Tilbage til oversigten](Home-da)

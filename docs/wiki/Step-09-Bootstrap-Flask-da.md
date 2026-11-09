[English](Step-09-Bootstrap-Flask) · **Dansk** · [Bahasa Malaysia](Step-09-Bootstrap-Flask-ms)

# Trin 9: Bootstrap-Flask

## Hvad lektionen bad om

Installér `bootstrap-flask`, initialisér den i appen, indlæs Bootstrap-CSS i `base.html` og konvertér alle fire sider.

## Hvad vi byggede

`Bootstrap5(app)` oprettes i indgangspunktet, og `base.html` kalder `bootstrap.load_css()`. Vi serverer Bootstrap-filerne fra vores eget site, så siderne virker uden CDN.

```
bootstrap = Bootstrap5(app)

<head>
    {{ bootstrap.load_css() }}
</head>
```

## Sådan ser det ud

![Trin 9: Bootstrap-Flask](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-09-bootstrap-flask.png)

![Trin 9: Bootstrap-Flask](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-09-bootstrap-home.png)

## Hvad vi lærte

- En udvidelse kan give et moderne udseende med meget lidt kode.
- Forældreskabelonen betaler sig: én linje i `base.html` styler alle sider.
- At servere filer lokalt undgår en forespørgsel til en tredjepart.

Forrige trin: [Super-blokke](Step-08-Super-Blocks-da) · Næste trin: [render_form](Step-10-Render-Form-da) · [Tilbage til oversigten](Home-da)

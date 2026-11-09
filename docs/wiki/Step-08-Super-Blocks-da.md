[English](Step-08-Super-Blocks) · **Dansk** · [Bahasa Malaysia](Step-08-Super-Blocks-ms)

# Trin 8: Super-blokke

## Hvad lektionen bad om

Giv alle sider en lilla baggrund fra en `styling`-blok i `base.html`, og gør overskriften rød på afvist-siden med `{{ super() }}`.

## Hvad vi byggede

Afvist-siden overskriver `styling`-blokken, kalder `super()` for at beholde den lilla baggrund og tilføjer en rød `h1`. Trin 9 erstatter denne styling med Bootstrap.

```
{% block styling %}
{{ super() }}
h1 {
    color: red;
}
{% endblock %}
```

## Sådan ser det ud

![Trin 8: Super-blokke](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-08-super-block.png)

## Hvad vi lærte

- `super()` beholder det, forældreblokken rummer, og lader barnet tilføje til det.
- Et barn kan ændre én detalje uden at kopiere hele forælderen.
- Styling kan deles og stadig justeres pr. side.

Forrige trin: [Skabelonarv](Step-07-Template-Inheritance-da) · Næste trin: [Bootstrap-Flask](Step-09-Bootstrap-Flask-da) · [Tilbage til oversigten](Home-da)

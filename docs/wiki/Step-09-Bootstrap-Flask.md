**English** · [Dansk](Step-09-Bootstrap-Flask-da) · [Bahasa Malaysia](Step-09-Bootstrap-Flask-ms)

# Step 9: Bootstrap-Flask

## What the lecture asked

Install `bootstrap-flask`, initialise it in the app, load the Bootstrap CSS in `base.html` and convert all four pages.

## What we built

`Bootstrap5(app)` is created in the entry point and `base.html` calls `bootstrap.load_css()`. We serve the Bootstrap files from our own site, so the pages work without a CDN.

```
bootstrap = Bootstrap5(app)

<head>
    {{ bootstrap.load_css() }}
</head>
```

## What it looks like

![Step 9: Bootstrap-Flask](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-09-bootstrap-flask.png)

![Step 9: Bootstrap-Flask](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-09-bootstrap-home.png)

## What we gained

- An extension can give a modern look with very little code.
- The parent template pays off: one line in `base.html` styles every page.
- Serving files locally avoids a request to a third party.

Previous step: [Super blocks](Step-08-Super-Blocks) · Next step: [render_form](Step-10-Render-Form) · [Back to the overview](Home)

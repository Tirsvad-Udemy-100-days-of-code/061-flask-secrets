**English** · [Dansk](Step-10-Render-Form-da) · [Bahasa Malaysia](Step-10-Render-Form-ms)

# Step 10: render_form

## What the lecture asked

Replace the hand-written form with `render_form(form)` from Bootstrap-Flask.

## What we built

One line draws the labels, inputs, button, CSRF token and error messages. The input size 30 is kept with `render_kw` in the form class.

```
{% from 'bootstrap5/form.html' import render_form %}
{{ render_form(form, action=url_for('login'), novalidate=True) }}
```

## What it looks like

![Step 10: render_form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-10-render-form.png)

## What we gained

- A macro can replace dozens of lines of HTML.
- It helps to know how the form works under the hood before using the shortcut, so a broken form can be debugged.
- Field settings such as the size belong in the form class, where every renderer can use them.

Previous step: [Bootstrap-Flask](Step-09-Bootstrap-Flask) · [Back to the overview](Home)

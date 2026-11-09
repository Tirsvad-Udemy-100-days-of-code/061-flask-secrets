**English** · [Dansk](Step-07-Template-Inheritance-da) · [Bahasa Malaysia](Step-07-Template-Inheritance-ms)

# Step 7: Template inheritance

## What the lecture asked

Create `base.html` with blocks and let `success.html` and `denied.html` extend it.

## What we built

`base.html` has a `title` block and a `content` block. The child pages start with `{% extends "base.html" %}` and fill the blocks.

```
{% extends "base.html" %}
{% block title %}Success{% endblock %}
{% block content %}
<h1>Top Secret</h1>
{% endblock %}
```

## What it looks like

![Step 7: Template inheritance](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-07-base-template.png)

## What we gained

- One parent template holds the shared page frame, so it is written once.
- `extends` suits pages that share a design; `include` suits small shared pieces.
- A change to the frame reaches every page.

Previous step: [Check the credentials](Step-06-Check-Credentials) · Next step: [Super blocks](Step-08-Super-Blocks) · [Back to the overview](Home)

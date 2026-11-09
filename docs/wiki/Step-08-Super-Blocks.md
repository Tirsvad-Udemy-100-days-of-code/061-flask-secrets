**English** · [Dansk](Step-08-Super-Blocks-da) · [Bahasa Malaysia](Step-08-Super-Blocks-ms)

# Step 8: Super blocks

## What the lecture asked

Give every page a purple background from a `styling` block in `base.html`, and make the heading red on the denied page with `{{ super() }}`.

## What we built

The denied page overrides the `styling` block, calls `super()` to keep the purple background and adds a red `h1`. Step 9 replaces this styling with Bootstrap.

```
{% block styling %}
{{ super() }}
h1 {
    color: red;
}
{% endblock %}
```

## What it looks like

![Step 8: Super blocks](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-08-super-block.png)

## What we gained

- `super()` keeps what the parent block holds and lets the child add to it.
- A child can change one detail without copying the whole parent.
- Styling can be shared and still be adjusted per page.

Previous step: [Template inheritance](Step-07-Template-Inheritance) · Next step: [Bootstrap-Flask](Step-09-Bootstrap-Flask) · [Back to the overview](Home)

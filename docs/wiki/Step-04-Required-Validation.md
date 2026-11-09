**English** · [Dansk](Step-04-Required-Validation-da) · [Bahasa Malaysia](Step-04-Required-Validation-ms)

# Step 4: Required fields and novalidate

## What the lecture asked

Add `DataRequired`, show `form.<field>.errors`, accept POST with `validate_on_submit()` and switch off browser validation with `novalidate`.

## What we built

Both fields have a `DataRequired` validator. The route accepts GET and POST. Errors are printed in red beside the field.

```
email = StringField(label="Email", validators=[DataRequired()])

if form.validate_on_submit():
    ...
```

## What it looks like

![Step 4: Required fields and novalidate](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-04-required-validation.png)

## What we gained

- Validators check input without our own code.
- `validate_on_submit()` is false on a GET request and when a validator fails.
- `novalidate` gives every browser the same messages, so we can test them.

Previous step: [Five code improvements](Step-03-Code-Improvements) · Next step: [Email and length validation](Step-05-Email-And-Length-Validation) · [Back to the overview](Home)

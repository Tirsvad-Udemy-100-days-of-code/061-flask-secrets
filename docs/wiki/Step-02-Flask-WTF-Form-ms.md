[English](Step-02-Flask-WTF-Form) · [Dansk](Step-02-Flask-WTF-Form-da) · **Bahasa Malaysia**

# Langkah 2: Borang log masuk dengan Flask-WTF

## Apa yang diminta oleh kuliah

Bina borang dengan medan e-mel dan kata laluan (kedua-duanya `StringField`, saiz 30) serta perlindungan CSRF, tanpa menulis `<label>` atau `<input>` secara manual.

## Apa yang kami bina

`LoginForm` mewarisi `FlaskForm`. Templat mencetak `form.csrf_token` dan setiap medan. Aplikasi mempunyai kunci rahsia yang menandatangani token.

```
class LoginForm(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")
```

## Rupa hasilnya

![Langkah 2: Borang log masuk dengan Flask-WTF](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-02-flask-wtf-form.png)

## Apa yang kami peroleh

- Borang ialah kelas Python, dan pewarisan kelas memberikan tingkah lakunya.
- Token CSRF dan kunci rahsia menghalang laman lain daripada menghantar data atas nama pengguna.
- Templat melukis medan daripada objek borang, jadi HTML kekal ringkas.

Langkah sebelumnya: [Laluan log masuk](Step-01-Login-Route-ms) · Langkah seterusnya: [Lima penambahbaikan kod](Step-03-Code-Improvements-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

[English](Step-01-Login-Route) · [Dansk](Step-01-Login-Route-da) · **Bahasa Malaysia**

# Langkah 1: Laluan log masuk

## Apa yang diminta oleh kuliah

Cipta laluan `login` yang memaparkan `login.html`.

## Apa yang kami bina

Fungsi `login` memaparkan templat dan didaftarkan pada `/login`. Halaman utama `home` didaftarkan pada `/`.

```
def login() -> str:
    return render_template("login.html")

app.add_url_rule("/login", endpoint="login", view_func=login)
```

## Rupa hasilnya

![Langkah 1: Laluan log masuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-01-login-route.png)

## Apa yang kami peroleh

- Laluan Flask menghubungkan URL dengan fungsi Python.
- `render_template` mencari fail HTML dalam folder `templates`.
- Menyimpan laluan dalam pakej `presentation` mengasingkan bahagian web daripada peraturan.

Langkah seterusnya: [Borang log masuk dengan Flask-WTF](Step-02-Flask-WTF-Form-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

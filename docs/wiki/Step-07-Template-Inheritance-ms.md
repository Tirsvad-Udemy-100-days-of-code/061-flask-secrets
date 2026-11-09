[English](Step-07-Template-Inheritance) · [Dansk](Step-07-Template-Inheritance-da) · **Bahasa Malaysia**

# Langkah 7: Pewarisan templat

## Apa yang diminta oleh kuliah

Cipta `base.html` dengan blok dan biarkan `success.html` serta `denied.html` memanjangkannya.

## Apa yang kami bina

`base.html` mempunyai blok `title` dan blok `content`. Halaman anak bermula dengan `{% extends "base.html" %}` dan mengisi blok.

```
{% extends "base.html" %}
{% block title %}Success{% endblock %}
{% block content %}
<h1>Top Secret</h1>
{% endblock %}
```

## Rupa hasilnya

![Langkah 7: Pewarisan templat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-07-base-template.png)

## Apa yang kami peroleh

- Satu templat induk memegang rangka halaman yang dikongsi, jadi ia ditulis sekali.
- `extends` sesuai untuk halaman dengan reka bentuk sama; `include` sesuai untuk bahagian kecil yang dikongsi.
- Perubahan pada rangka sampai kepada semua halaman.

Langkah sebelumnya: [Semak bukti kelayakan](Step-06-Check-Credentials-ms) · Langkah seterusnya: [Blok super](Step-08-Super-Blocks-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

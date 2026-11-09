[English](Step-10-Render-Form) · [Dansk](Step-10-Render-Form-da) · **Bahasa Malaysia**

# Langkah 10: render_form

## Apa yang diminta oleh kuliah

Gantikan borang tulisan tangan dengan `render_form(form)` daripada Bootstrap-Flask.

## Apa yang kami bina

Satu baris melukis label, input, butang, token CSRF dan mesej ralat. Saiz input 30 dikekalkan dengan `render_kw` dalam kelas borang.

```
{% from 'bootstrap5/form.html' import render_form %}
{{ render_form(form, action=url_for('login'), novalidate=True) }}
```

## Rupa hasilnya

![Langkah 10: render_form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-10-render-form.png)

## Apa yang kami peroleh

- Makro boleh menggantikan berpuluh baris HTML.
- Memahami cara borang berfungsi sebelum menggunakan jalan pintas membantu apabila borang rosak perlu dinyahpepijat.
- Tetapan medan seperti saiz tergolong dalam kelas borang, supaya setiap pemapar boleh menggunakannya.

Langkah sebelumnya: [Bootstrap-Flask](Step-09-Bootstrap-Flask-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

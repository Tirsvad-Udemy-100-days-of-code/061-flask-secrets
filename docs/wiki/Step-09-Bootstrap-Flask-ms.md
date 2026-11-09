[English](Step-09-Bootstrap-Flask) · [Dansk](Step-09-Bootstrap-Flask-da) · **Bahasa Malaysia**

# Langkah 9: Bootstrap-Flask

## Apa yang diminta oleh kuliah

Pasang `bootstrap-flask`, mulakannya dalam aplikasi, muatkan CSS Bootstrap dalam `base.html` dan tukar keempat-empat halaman.

## Apa yang kami bina

`Bootstrap5(app)` dicipta pada titik masuk dan `base.html` memanggil `bootstrap.load_css()`. Kami menyajikan fail Bootstrap daripada laman sendiri, jadi halaman berfungsi tanpa CDN.

```
bootstrap = Bootstrap5(app)

<head>
    {{ bootstrap.load_css() }}
</head>
```

## Rupa hasilnya

![Langkah 9: Bootstrap-Flask](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-09-bootstrap-flask.png)

![Langkah 9: Bootstrap-Flask](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-09-bootstrap-home.png)

## Apa yang kami peroleh

- Sambungan boleh memberi rupa moden dengan sangat sedikit kod.
- Templat induk membuahkan hasil: satu baris dalam `base.html` menggayakan semua halaman.
- Menyajikan fail secara setempat mengelakkan permintaan kepada pihak ketiga.

Langkah sebelumnya: [Blok super](Step-08-Super-Blocks-ms) · Langkah seterusnya: [render_form](Step-10-Render-Form-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

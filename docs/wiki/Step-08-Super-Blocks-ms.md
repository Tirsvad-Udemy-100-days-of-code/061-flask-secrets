[English](Step-08-Super-Blocks) · [Dansk](Step-08-Super-Blocks-da) · **Bahasa Malaysia**

# Langkah 8: Blok super

## Apa yang diminta oleh kuliah

Beri semua halaman latar belakang ungu daripada blok `styling` dalam `base.html`, dan jadikan tajuk merah pada halaman ditolak dengan `{{ super() }}`.

## Apa yang kami bina

Halaman ditolak menimpa blok `styling`, memanggil `super()` untuk mengekalkan latar ungu dan menambah `h1` merah. Langkah 9 menggantikan gaya ini dengan Bootstrap.

```
{% block styling %}
{{ super() }}
h1 {
    color: red;
}
{% endblock %}
```

## Rupa hasilnya

![Langkah 8: Blok super](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-08-super-block.png)

## Apa yang kami peroleh

- `super()` mengekalkan apa yang dipegang blok induk dan membenarkan anak menambah kepadanya.
- Anak boleh mengubah satu butiran tanpa menyalin seluruh induk.
- Gaya boleh dikongsi dan masih diselaraskan bagi setiap halaman.

Langkah sebelumnya: [Pewarisan templat](Step-07-Template-Inheritance-ms) · Langkah seterusnya: [Bootstrap-Flask](Step-09-Bootstrap-Flask-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

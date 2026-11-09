[English](Step-04-Required-Validation) · [Dansk](Step-04-Required-Validation-da) · **Bahasa Malaysia**

# Langkah 4: Medan wajib dan novalidate

## Apa yang diminta oleh kuliah

Tambah `DataRequired`, papar `form.<medan>.errors`, terima POST dengan `validate_on_submit()` dan matikan pengesahan pelayar dengan `novalidate`.

## Apa yang kami bina

Kedua-dua medan mempunyai pengesah `DataRequired`. Laluan menerima GET dan POST. Ralat dipaparkan dengan warna merah di sebelah medan.

```
email = StringField(label="Email", validators=[DataRequired()])

if form.validate_on_submit():
    ...
```

## Rupa hasilnya

![Langkah 4: Medan wajib dan novalidate](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-04-required-validation.png)

## Apa yang kami peroleh

- Pengesah menyemak input tanpa kod kami sendiri.
- `validate_on_submit()` bernilai palsu pada permintaan GET dan apabila pengesah gagal.
- `novalidate` memberi mesej yang sama kepada semua pelayar, jadi kami boleh mengujinya.

Langkah sebelumnya: [Lima penambahbaikan kod](Step-03-Code-Improvements-ms) · Langkah seterusnya: [Pengesahan e-mel dan panjang](Step-05-Email-And-Length-Validation-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

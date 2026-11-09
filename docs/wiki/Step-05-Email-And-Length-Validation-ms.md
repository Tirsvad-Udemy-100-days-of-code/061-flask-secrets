[English](Step-05-Email-And-Length-Validation) · [Dansk](Step-05-Email-And-Length-Validation-da) · **Bahasa Malaysia**

# Langkah 5: Pengesahan e-mel dan panjang

## Apa yang diminta oleh kuliah

E-mel mestilah alamat yang sah dan kata laluan mesti sekurang-kurangnya 8 aksara.

## Apa yang kami bina

`Email()` dan `Length(min=8)` ditambah. `Email()` memerlukan pakej tambahan `email-validator`. Nombor 8 disimpan dalam `constants.py`.

```
password = PasswordField(
    label="Password",
    validators=[DataRequired(), Length(min=PASSWORD_MIN_LENGTH)],
)
```

## Rupa hasilnya

![Langkah 5: Pengesahan e-mel dan panjang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-05-email-and-length-validation.png)

## Apa yang kami peroleh

- Pengesah siap pakai menggantikan semakan kami sendiri untuk e-mel dan panjang.
- Sesetengah pengesah memerlukan pakej tambahan, dan dokumentasi menyatakannya.
- Pemalar dalam satu modul (`constants.py`) memastikan peraturan berada di satu tempat.

Langkah sebelumnya: [Medan wajib dan novalidate](Step-04-Required-Validation-ms) · Langkah seterusnya: [Semak bukti kelayakan](Step-06-Check-Credentials-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

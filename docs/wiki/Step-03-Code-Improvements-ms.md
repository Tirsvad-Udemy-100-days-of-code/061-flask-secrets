[English](Step-03-Code-Improvements) · [Dansk](Step-03-Code-Improvements-da) · **Bahasa Malaysia**

# Langkah 3: Lima penambahbaikan kod

## Apa yang diminta oleh kuliah

Gunakan `PasswordField`, namakan argumen `label`, bina action dengan `url_for`, susun medan dengan jadual dan gunakan `SubmitField`.

## Apa yang kami bina

Medan kata laluan menyembunyikan apa yang ditaip, butang datang daripada borang dan action mengikut nama laluan.

```
email = StringField(label="Email")
password = PasswordField(label="Password")
submit = SubmitField(label="Log In")
```

## Rupa hasilnya

![Langkah 3: Lima penambahbaikan kod](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-03-code-improvements.png)

## Apa yang kami peroleh

- Memilih jenis medan yang betul meningkatkan keselamatan dan penggunaan.
- URL yang dibina dengan `url_for` terus berfungsi apabila laluan berubah.
- HTML biasa di sekeliling medan WTForms memberi kawalan penuh ke atas reka letak.

Langkah sebelumnya: [Borang log masuk dengan Flask-WTF](Step-02-Flask-WTF-Form-ms) · Langkah seterusnya: [Medan wajib dan novalidate](Step-04-Required-Validation-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

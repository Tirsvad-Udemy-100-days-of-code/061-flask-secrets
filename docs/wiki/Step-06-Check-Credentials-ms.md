[English](Step-06-Check-Credentials) · [Dansk](Step-06-Check-Credentials-da) · **Bahasa Malaysia**

# Langkah 6: Semak bukti kelayakan

## Apa yang diminta oleh kuliah

Jika borang yang dihantar sah dan e-mel ialah `admin@email.com` serta kata laluan `12345678`, papar `success.html`; jika tidak, papar `denied.html`.

## Apa yang kami bina

Peraturan berada dalam lapisan `domain` (`Credentials.is_admin`), kes guna `authenticate_user` dalam lapisan `application` dan laluan hanya memanggilnya. Akaun itu demo kuliah, bukan bukti kelayakan sebenar.

```
if form.validate_on_submit():
    if authenticate_user(form.email.data, form.password.data):
        return render_template("success.html")
    return render_template("denied.html")
```

## Rupa hasilnya

![Langkah 6: Semak bukti kelayakan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-06-success.png)

![Langkah 6: Semak bukti kelayakan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/raw/branch/main/docs/images/step-06-denied.png)

## Apa yang kami peroleh

- `form.<medan>.data` memberi nilai yang ditaip pengguna.
- Hasil `validate_on_submit()` membezakan penghantaran daripada paparan halaman biasa.
- Peraturan perniagaan boleh berada di luar Flask dan diuji bersendirian; perbandingan berjalan dalam masa tetap.

Langkah sebelumnya: [Pengesahan e-mel dan panjang](Step-05-Email-And-Length-Validation-ms) · Langkah seterusnya: [Pewarisan templat](Step-07-Template-Inheritance-ms) · [Kembali ke gambaran keseluruhan](Home-ms)

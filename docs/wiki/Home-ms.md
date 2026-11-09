[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Flask Secrets: Hari 61, borang lanjutan

Wiki ini menerangkan apa yang diajar oleh setiap langkah kuliah Hari 61 kursus Udemy "100 Days of Code: The Complete Python Pro Bootcamp". Kami membina laman Flask dengan borang log masuk yang hanya menunjukkan halaman rahsia kepada pengguna yang betul.

## Jalankan

Cipta `.venv` setempat, naik taraf pip, pasang projek dan mulakannya (arahan penuh ada dalam [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m flask_secrets.presentation.main
```

Akaun `admin@email.com` dengan kata laluan `12345678` ialah demo kuliah, bukan bukti kelayakan sebenar.

## Sepuluh langkah

1. [Langkah 1: Laluan log masuk](Step-01-Login-Route-ms)
2. [Langkah 2: Borang log masuk dengan Flask-WTF](Step-02-Flask-WTF-Form-ms)
3. [Langkah 3: Lima penambahbaikan kod](Step-03-Code-Improvements-ms)
4. [Langkah 4: Medan wajib dan novalidate](Step-04-Required-Validation-ms)
5. [Langkah 5: Pengesahan e-mel dan panjang](Step-05-Email-And-Length-Validation-ms)
6. [Langkah 6: Semak bukti kelayakan](Step-06-Check-Credentials-ms)
7. [Langkah 7: Pewarisan templat](Step-07-Template-Inheritance-ms)
8. [Langkah 8: Blok super](Step-08-Super-Blocks-ms)
9. [Langkah 9: Bootstrap-Flask](Step-09-Bootstrap-Flask-ms)
10. [Langkah 10: render_form](Step-10-Render-Form-ms)

## Apa yang kami peroleh secara keseluruhan

- Borang sebagai kelas Python dengan Flask-WTF, termasuk perlindungan CSRF.
- Pengesah siap pakai dan mesej ralat yang jelas.
- Pewarisan templat dan Bootstrap-Flask untuk reka bentuk yang seragam.
- Peraturan perniagaan diasingkan daripada Flask dan dilindungi oleh ujian pytest.

# Bot Kursus Coursera Otomatis
## [Bot 100% Menandai Modul Video dan Bacaan]

Skrip Python ini mengotomatiskan interaksi dengan kursus Coursera, termasuk menandai video dan bacaan sebagai selesai, dan menavigasi melalui konten kursus. Skrip ini mendukung penggunaan **Remote Desktop Protocol (RDP)** di GitHub dan menggunakan Selenium untuk otomatisasi peramban.

---

## Fitur
- **Login Otomatis**: Login secara manual sekali dan simpan cookie untuk sesi mendatang.
- **Navigasi Kursus**: Navigasi otomatis melalui modul kursus dan tandai item sebagai selesai.
- **Dukungan Multi-kursus**: Memproses beberapa kursus secara bersamaan dengan memasukkan serangkaian tautan kursus.
- **Integrasi Tombol Pintasan**: Gunakan `Ctrl + C` untuk menghentikan putaran otomatisasi.

---

## BUAT RDP MENGGUNAKAN GITHUB
### Pakai RDP agar jaringannya cepat dan ngga lambat
Anda dapat memeriksa tutorial di repositori saya tentang [RDP Github Gratis](https://github.com/fikriarmiafahmi/freeRDP).
### Lalu, jalankan RDP dan instal persyaratan di bawah ini ke dalam RDP
---
## Petunjuk Penggunaan
1. Klon Repositori
   ```bash
   git clone https://github.com/fikriarmiafahmi/coursera-bot.git
   cd coursera-bot
   ```
2. Konfigurasikan Kredensial Pengguna
   Perbarui variabel berikut dalam skrip `env.py`:
   ```python
   USERNAME = "your-email@example.com"
   PASSWORD = "your-password"
   ```
3. Jalankan Skrip
   ```bash
   python coursera.py
   ```
4. Masukkan Tautan Kursus
   Saat diminta, masukkan tautan kursus Coursera sebagai daftar yang dipisahkan spasi:
   ```text
   Masukkan tautan course (Banyak tautan, pisahkan dengan spasi): link1 link2 link3
   ```
   ## CATATAN:
   Gunakan tautan yang ada di awal course/introduction
   contohnya seperti ini:
   <br>https://www.coursera.org/learn/introduction-to-databases/home/module/1
   <br>Atau
   <br>https://www.coursera.org/learn/introduction-to-databases/home/module/2
   <br>dll
---

## Penggunaan Tombol Pintasan
Hentikan Otomatisasi: Tekan `Ctrl + C` untuk menghentikan proses saat ini.
## Keterbatasan
Memerlukan login manual untuk menjalankan pertama guna menyimpan cookie.
Dikonfigurasi khusus untuk kursus Coursera; sesuaikan pemilih XPath atau CSS jika UI berubah.

---

# SANGGAHAN!!!
```hash
Sanggahan Tanggung Jawab:
Skrip ini disediakan untuk tujuan pendidikan dan informasi saja.
Penulis tidak bertanggung jawab atas penyalahgunaan, kerusakan, atau konsekuensi hukum
yang mungkin timbul dari penggunaan perangkat lunak ini. Pengguna bertanggung jawab untuk mematuhi semua hukum dan ketentuan layanan yang berlaku pada platform yang terlibat.
```
---
---
# Automated Coursera Course Bot
## [Bot 100% Marked Video and Reading Module]

This Python script automates interactions with Coursera courses, including marking videos and readings as completed, and navigating through course content. It supports **Remote Desktop Protocol (RDP)** usage on GitHub and uses Selenium for browser automation.

---

## Features
- **Automated Login**: Login manually once and save cookies for future sessions.
- **Course Navigation**: Automatically navigate through course modules and mark items as completed.
- **Multi-course Support**: Process multiple courses simultaneously by inputting an array of course links.
- **Hotkey Integration**: Use `Ctrl + C` to stop the automation loop.

---

## CREATE RDP USING GITHUB
### Pakai RDP agar jaringannya fast dan ngga lambat
You can check tutorial on my repository about [Free RDP Github](https://github.com/fikriarmiafahmi/freeRDP).
### And then, run RDP and install requirements on below into the RDP
---
## Usage Instructions
1. Clone the Repository
   ```bash
   git clone https://github.com/fikriarmiafahmi/coursera-bot.git
   cd coursera-bot
   ```
2. Configure User Credentials
   Update the following variables in the script `env.py`:
   ```python
   USERNAME = "your-email@example.com"
   PASSWORD = "your-password"
   ```
3. Run the Script
   ```bash
   python coursera.py
   ```

4. Input Course Links
   When prompted, input the Coursera course links as a space-separated list:
   ```text
   Input link course (Banyak link, pisahkan dengan spasi): link1 link2 link3
   ```
   ## NOTE:
   Use the link at the beginning of the course/introduction, for example like this:
   <br>https://www.coursera.org/learn/introduction-to-databases/home/module/1
   <br>Or
   <br>https://www.coursera.org/learn/introduction-to-databases/home/module/2
   <br>etc.
---

## Hotkey Usage
Stop Automation: Press `Ctrl + C` to stop the current process.
## Limitations
Requires manual login for the first run to save cookies.
Configured specifically for Coursera courses; adjust XPath or CSS selectors if UI changes.

---

# DISCLAIMER!!!
```hash
Disclaimer of Liability:
This script is provided for educational and informational purposes only.
The author is not responsible for any misuse, damage, or legal consequences
that may arise from the use of this software. Users are responsible for
complying with all applicable laws and terms of service of the platforms
involved.
```

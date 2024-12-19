# Image Color Detector 🔴🟠🟡🟢🔵🟣
Scripting Language 2024

Image Color Detector adalah aplikasi desktop berbasis Python dengan antarmuka grafis (GUI) untuk mendeteksi warna dominan dari sebuah gambar. Aplikasi ini memungkinkan pengguna untuk memilih gambar dan menampilkan palet warna utama beserta kode warna dalam format hexadecimal.

## Fitur Utama

- **Pilih Gambar**: Pilih gambar dari penyimpanan lokal untuk analisis warna.
- **Deteksi Warna**: Tampilkan hingga 12 warna dominan dari gambar yang dipilih.
- **Antarmuka Interaktif**: Tampilkan warna dominan dalam bentuk lingkaran warna dan label hexadecimal.
- **Dukungan Format Gambar**: Mendukung berbagai format gambar seperti `.jpg`, `.jpeg`, `.png`, `.bmp`, dan `.gif`.

## Teknologi yang Digunakan

- **Python 3.x**
- **Tkinter**: Untuk antarmuka pengguna (GUI).
- **Pillow (PIL)**: Untuk pemrosesan gambar.
- **ColorThief**: Untuk ekstraksi warna dominan dari gambar.

## Cara Instalasi

1. Clone repository ini ke komputer lokal Anda:
    ```bash
    git clone https://github.com/danendradipa/color-detection.git
    ```

2. Instal library yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

## Cara Menjalankan
Untuk menjalankan aplikasi, Anda bisa menggunakan cara berikut:

1. Dari root direktori proyek:
    ```bash
    python color_detection.py
    ```

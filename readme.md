# Twitter Scraping Tool

## Deskripsi
Tool ini dibuat untuk mengekstrak data tweet terbaru dari Twitter (X.com) berdasarkan kata kunci pencarian. Tool menggunakan Selenium untuk otomatisasi browser dan menyimpan hasil ekstraksi dalam format CSV.

## Fitur
- Pencarian tweet berdasarkan kata kunci
- Pengaturan jumlah tweet yang akan diambil
- Ekstraksi informasi penting dari tweet:
  - Username
  - Tweet ID
  - Isi tweet
  - Waktu tweet
- Penyimpanan hasil dalam format CSV

## Prasyarat
Sebelum menggunakan tool ini, pastikan Anda telah menginstal:
1. Python 3.6 atau lebih baru
2. Selenium
3. Chrome WebDriver (sesuai dengan versi Chrome Anda)

## Instalasi
1. Clone repository ini:
   ```
   git clone https://github.com/admiralkuznetsov45/scrapping-twitter.git
   cd scrapping-twitter
   ```

2. Instal dependensi yang diperlukan:
   ```
   pip install selenium
   pip install nest_asyncio
   ```

3. Download Chrome WebDriver dari [situs resmi](https://sites.google.com/chromium.org/driver/) dan pastikan sesuai dengan versi Chrome Anda.

## Cara Penggunaan
1. Pastikan Anda sudah login ke akun Twitter Anda di browser Chrome (jika diperlukan).

2. Jalankan script:
   ```
   jupyter notebook script-twitter.ipynb
   ```
   atau
   ```
   python test.py
   ```

3. Ikuti petunjuk di terminal:
   - Masukkan kata kunci yang ingin dicari (misalnya: "bakso", "politik", dll)
   - Masukkan jumlah tweet yang ingin diambil (misalnya: 10, 20, dll)

4. Script akan otomatis:
   - Membuka browser Chrome
   - Menavigasi ke Twitter
   - Memasukkan kata kunci pencarian
   - Mengklik tab "Terbaru"
   - Mengekstrak data dari tweet yang muncul
   - Menyimpan data ke file CSV

5. Hasil akan disimpan dalam file CSV dengan format nama: `twitter_tweets_YYYYMMDD_HHMMSS.csv`

## Struktur Data CSV
File CSV yang dihasilkan akan memiliki kolom-kolom berikut:
- `position`: Posisi tweet dalam hasil pencarian
- `username`: Nama pengguna yang membuat tweet
- `tweet_id`: ID unik dari tweet
- `tweet_text`: Isi teks dari tweet
- `tweet_time`: Waktu tweet dibuat (format ISO)

## Troubleshooting
- **XPath Error**: Jika terjadi error terkait XPath, kemungkinan Twitter telah mengubah struktur HTML-nya. Perbarui XPath dalam kode.
- **Element Not Found**: Pastikan Anda memiliki koneksi internet yang stabil dan Twitter dapat diakses.
- **Login Required**: Jika Twitter meminta login, login secara manual sebelum menjalankan script.

## Catatan Penting
- Tool ini dibuat untuk tujuan pendidikan dan penelitian.
- Penggunaan scraping harus mematuhi Terms of Service dari Twitter.
- Twitter dapat mengubah struktur HTML-nya kapan saja, yang mungkin menyebabkan script ini tidak berfungsi.
- Gunakan dengan bijak dan bertanggung jawab.

## Kontribusi
Kontribusi untuk perbaikan dan pengembangan tool ini sangat diterima. Silakan buat pull request atau laporkan issue jika Anda menemukan bug atau memiliki saran perbaikan.

## Lisensi
[MIT License](LICENSE)


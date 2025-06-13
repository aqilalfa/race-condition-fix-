# Race Condition Fix (Flask App)

Proyek ini adalah perbaikan dari aplikasi Flask sederhana yang rentan terhadap **race condition** saat beberapa pengguna mencoba membeli stok barang secara bersamaan.

## 📦 Fitur

- Endpoint `/buy` untuk membeli item menggunakan metode POST
- Penanganan file `stock.txt` secara **thread-safe** menggunakan file locking
- Script `race_attack.py` untuk menguji race condition
- Reset stok otomatis ke nilai awal (10) saat server dijalankan

## 🚀 Cara Menjalankan

1. pip install -r requirements.txt
2. python app.py
3. python race_attack.py

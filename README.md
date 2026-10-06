# Pertemuan 06 - Nested Loop, Pola, Akumulasi, dan Pencacahan

Nama : Sri Nur Rahmawati  
NIM : 2225250182  
Kelas : 3F

---

## Tujuan

Praktikum ini bertujuan untuk memahami penggunaan nested loop dalam Python untuk membentuk pola, menghasilkan pasangan data, melakukan akumulasi, serta melakukan pencacahan berdasarkan kondisi tertentu.

Melalui latihan dan tugas yang dikerjakan, mahasiswa diharapkan mampu:

- Memahami hubungan loop luar dan loop dalam.
- Membuat pola menggunakan nested loop.
- Menghitung jumlah data menggunakan akumulator.
- Menghitung banyak kejadian menggunakan counter.
- Menghitung jumlah iterasi nested loop.
- Menguji program menggunakan beberapa test case.
- Mengelola file proyek menggunakan Git dan GitHub.

---

## Tujuan Penggunaan Nested Loop

Nested loop digunakan ketika program memerlukan dua proses perulangan yang saling berhubungan, misalnya:

- Membuat tabel perkalian.
- Membuat pola segitiga.
- Menampilkan pasangan indeks.
- Menghitung pasangan yang memenuhi kondisi tertentu.
- Melakukan akumulasi per baris dan keseluruhan.

Loop luar bertugas mengatur baris atau kelompok data, sedangkan loop dalam memproses isi dari setiap baris.

---

## Pola, Akumulasi, dan Pencacahan

### Pola
Pola dibuat dengan mengatur jumlah perulangan pada loop dalam berdasarkan nilai loop luar.

### Akumulasi
Akumulasi digunakan untuk menjumlahkan nilai, baik per baris maupun seluruh data.

Contoh:
- total_baris
- total_semua

### Pencacahan
Pencacahan digunakan untuk menghitung banyak data yang memenuhi syarat tertentu.

Contoh:
- count
- count_genap

---

## Cara Menjalankan Program

Pastikan Python 3 telah terpasang.

Cek versi Python:

```bash
python --version
# Praktikum Pertemuan 5 — Struktur Data Python

Program Studi Sistem Informasi — Pemrograman Python

**Disusun oleh:** Ahmad Sahrul F — NPM 20241320031

## Isi

| File | Keterangan |
|---|---|
| `Praktikum_Struktur_Data.py` | Program utama (5 soal praktik, berbentuk menu) |
| `contoh_teks.txt` | Teks contoh untuk Soal 5 |
| `bukti_praktikum_soal1-3.png` | Bukti hasil run Soal 1–3 |
| `bukti_praktikum_soal4-5.png` | Bukti hasil run Soal 4–5 |

## Jawaban Soal Teori

**1. Perbedaan list dan tuple.**
List bersifat *mutable* (isinya bisa diubah, ditambah, dihapus) dan ditulis dengan kurung siku `[]`. Tuple bersifat *immutable* (tidak bisa diubah setelah dibuat) dan ditulis dengan kurung biasa `()`. Karena immutable, tuple sedikit lebih cepat dan bisa dipakai sebagai kunci dictionary.
- Tuple lebih tepat untuk data yang tetap dan tidak boleh berubah, misalnya nama hari (`("Senin", "Selasa", ...)`), koordinat `(x, y)`, atau data konfigurasi.
- List lebih tepat untuk koleksi dinamis, misalnya daftar nilai mahasiswa yang bisa bertambah, daftar belanja, atau hasil query database.

**2. Mengapa set tidak mendukung pengindeksan?**
Set diimplementasikan dengan *hash table*: setiap elemen disimpan berdasarkan nilai hash-nya, bukan berdasarkan urutan penambahan. Akibatnya set bersifat *unordered* — tidak ada urutan posisi yang tetap. Pengindeksan seperti `s[0]` butuh posisi yang stabil ("elemen ke-0"), yang tidak ada pada set. Keanggotaan dicek lewat hash, bukan lewat posisi.

**3. Apa itu hashable?**
Hashable artinya objek memiliki nilai hash yang tetap selama hidupnya, sehingga bisa ditempatkan dan dicari di hash table.
- Hashable: `int`, `str`, `float`, `tuple` (jika semua isinya hashable), `frozenset`, `bool`.
- Tidak hashable: `list`, `dict`, `set`, `bytearray` (semuanya mutable — isinya bisa berubah).
- Kunci dictionary harus hashable karena dictionary menyimpan dan mencari nilai lewat hash kuncinya. Jika kunci bisa berubah, nilai hash-nya ikut berubah dan datanya menjadi tidak bisa ditemukan.

**4. Mengapa `in` pada set O(1) sedangkan pada list O(n)?**
Pada set, operator `in` menghitung hash dari nilai lalu langsung melompat ke lokasi penyimpanannya — tidak peduli berapa banyak elemen, waktunya rata-rata tetap (O(1)). Pada list, Python harus memeriksa elemen satu per satu dari awal sampai ketemu (O(n)).
- Implikasi praktis: untuk data besar (misalnya 1 juta ID) dengan pencarian berulang, set bisa ribuan kali lebih cepat. Contoh: menyimpan ID yang sudah terdaftar dalam set, lalu mengecek `id_baru in terdaftar`.

**5. Perbedaan `sort()` dan `sorted()`.**
- `list.sort()`: metode milik list, mengurutkan **di tempat** (list aslinya berubah), mengembalikan `None`, hanya bisa dipakai pada list.
- `sorted()`: fungsi bawaan, mengembalikan **list baru** yang sudah terurut tanpa mengubah data asli, bisa dipakai pada iterable apa pun (list, tuple, set, dictionary).
- Gunakan `sort()` jika list asli memang boleh diubah (lebih hemat memori). Gunakan `sorted()` jika data asli harus dipertahankan atau datanya bukan list (misalnya mengurutkan tuple tanpa mengubahnya).

## Soal Praktik

1. **String** — analisis kalimat: jumlah kata, jumlah karakter, kata terpanjang, title case.
2. **List & Dictionary** — nilai mahasiswa: rata-rata, nilai tertinggi/terendah, kategori A–E, frekuensi kategori.
3. **Set** — operasi himpunan penerima beasiswa: irisan, selisih, gabungan.
4. **Dictionary + Tuple** — inventaris toko: tambah barang, update stok, cari rentang harga, total nilai.
5. **Analisis teks file** — frekuensi kata, 10 kata tersering, hapax legomena, type-token ratio.

## Cara Menjalankan

```bash
python Praktikum_Struktur_Data.py
```

Lalu pilih nomor soal (1–5). File `contoh_teks.txt` harus berada di folder yang sama.

## Bukti Hasil Run

Soal 1–3 (analisis kalimat, nilai mahasiswa, beasiswa):

<img width="1000" height="647" alt="bukti_praktikum_soal1-3" src="https://github.com/user-attachments/assets/de0d8303-848f-4200-a01f-1da04692f3a2" />

Soal 4–5 (inventaris toko, analisis teks):

![Bukti run Soal 4–5](bukti_praktikum_soal4-5.png)<img width="1000" height="670" alt="bukti_praktikum_soal4-5" src="https://github.com/user-attachments/assets/d5f13462-380d-46c2-bcc6-a7745ef998ae" />


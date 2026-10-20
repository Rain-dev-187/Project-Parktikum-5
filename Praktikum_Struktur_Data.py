"""
PRAKTIKUM — String, List, Tuple, Set, Dictionary & Pemilihan Struktur Data
Pertemuan 5 — Program Studi Sistem Informasi
Disusun oleh: Ahmad Sahrul F — NPM 20241320031

Berisi 5 soal praktik. Jalankan: python Praktikum_Struktur_Data.py
lalu pilih nomor soal (1-5), atau 0 untuk menjalankan semuanya.
"""

import string as _string


# ============ SOAL 1: Operasi String ============
def soal1():
    print("\n=== SOAL 1: Analisis Kalimat (String) ===")
    kalimat = input("Masukkan sebuah kalimat: ").strip()
    kata = kalimat.split()

    jumlah_kata = len(kata)
    jumlah_karakter = len(kalimat)
    kata_terpanjang = max(kata, key=len) if kata else "-"
    title_case = kalimat.title()

    print(f"(a) Jumlah kata      : {jumlah_kata}")
    print(f"(b) Jumlah karakter : {jumlah_karakter}")
    print(f"(c) Kata terpanjang  : {kata_terpanjang}")
    print(f"(d) Title case       : {title_case}")


# ============ SOAL 2: List Nilai + Dictionary Frekuensi ============
def kategori(nilai):
    if nilai >= 85: return "A"
    if nilai >= 70: return "B"
    if nilai >= 55: return "C"
    if nilai >= 40: return "D"
    return "E"

def soal2():
    print("\n=== SOAL 2: Nilai Mahasiswa (List & Dictionary) ===")
    mentah = input("Masukkan nilai (pisahkan koma), contoh 85,70,90: ")
    nilai = [float(x.strip()) for x in mentah.split(",") if x.strip()]

    rata = sum(nilai) / len(nilai)
    tertinggi, terendah = max(nilai), min(nilai)

    frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for n in nilai:
        frekuensi[kategori(n)] += 1

    print(f"(a) Rata-rata            : {rata:.2f}")
    print(f"(b) Tertinggi / Terendah : {tertinggi:g} / {terendah:g}")
    print(f"(c) Kategori per nilai   : {[ (n, kategori(n)) for n in nilai ]}")
    print(f"(d) Frekuensi kategori   : {frekuensi}")


# ============ SOAL 3: Operasi Set ============
def soal3():
    print("\n=== SOAL 3: Beasiswa (Set) ===")
    a = input("ID penerima beasiswa A (pisahkan koma): ").split(",")
    b = input("ID penerima beasiswa B (pisahkan koma): ").split(",")
    A = {x.strip() for x in a if x.strip()}
    B = {x.strip() for x in b if x.strip()}

    print(f"(a) Kedua beasiswa        : {sorted(A & B)}")
    print(f"(b) Hanya beasiswa A      : {sorted(A - B)}")
    print(f"(c) Beasiswa B tapi bukan A: {sorted(B - A)}")
    print(f"(d) Semua penerima unik   : {sorted(A | B)}")


# ============ SOAL 4: Dictionary Inventaris ============
inventaris = {
    "Laptop": (8500000, 10),
    "Mouse": (150000, 50),
    "Keyboard": (350000, 30),
}

def tambah_barang(nama, harga, stok):
    inventaris[nama] = (harga, stok)
    print(f"Ditambah: {nama} (Rp{harga:,}, stok {stok})")

def update_stok(nama, stok_baru):
    if nama in inventaris:
        harga, _ = inventaris[nama]
        inventaris[nama] = (harga, stok_baru)
        print(f"Stok {nama} -> {stok_baru}")
    else:
        print(f"{nama} tidak ada di inventaris.")

def cari_rentang(harga_min, harga_max):
    hasil = {k: v for k, v in inventaris.items() if harga_min <= v[0] <= harga_max}
    return hasil

def total_nilai():
    return sum(harga * stok for harga, stok in inventaris.values())

def soal4():
    print("\n=== SOAL 4: Inventaris Toko (Dictionary + Tuple) ===")
    print("Data awal:", inventaris)
    tambah_barang("Monitor", 1800000, 15)          # (a)
    update_stok("Mouse", 45)                        # (b)
    print("(c) Harga Rp200rb-2jt:", cari_rentang(200000, 2000000))
    print(f"(d) Total nilai inventaris: Rp{total_nilai():,}")


# ============ SOAL 5: Analisis Teks dari File ============
def soal5(nama_file="contoh_teks.txt"):
    print("\n=== SOAL 5: Analisis Teks (String, List, Set, Dict) ===")
    with open(nama_file, encoding="utf-8") as f:
        teks = f.read().lower()
    # bersihkan tanda baca
    for t in _string.punctuation:
        teks = teks.replace(t, " ")
    kata = teks.split()

    frekuensi = {}
    for k in kata:
        frekuensi[k] = frekuensi.get(k, 0) + 1

    sepuluh = sorted(frekuensi.items(), key=lambda x: x[1], reverse=True)[:10]
    hapax = sorted({k for k, v in frekuensi.items() if v == 1})
    ttr = len(set(kata)) / len(kata) if kata else 0

    print(f"(a) Total kata: {len(kata)}, kata unik: {len(set(kata))}")
    print("(b) 10 kata tersering:")
    for k, v in sepuluh:
        print(f"    {k}: {v}")
    print(f"(c) Kata yang hanya muncul sekali ({len(hapax)}): {hapax[:15]}")
    print(f"(d) Type-token ratio: {ttr:.4f}")


# ============ MENU ============
def main():
    menu = {
        "1": soal1, "2": soal2, "3": soal3, "4": soal4, "5": soal5,
    }
    print("PRAKTIKUM STRUKTUR DATA PYTHON")
    print("1. Analisis kalimat (string)")
    print("2. Nilai mahasiswa (list & dict)")
    print("3. Beasiswa (set)")
    print("4. Inventaris toko (dict + tuple)")
    print("5. Analisis teks file")
    print("0. Jalankan semua (demo)")
    pilih = input("Pilih soal (0-5): ").strip()
    if pilih == "0":
        import io
        soal4()
        soal5()
        print("\n(Soal 1-3 butuh input manual — pilih nomornya langsung.)")
    elif pilih in menu:
        menu[pilih]()
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()

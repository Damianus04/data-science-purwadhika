# List Comprehension
# list_baru = [expression]

angka = [1, 2, 3, 4, 5]

pangkat = []
for i in angka:
    pangkat.append(i ** 2)

print(pangkat)

pangkat2 = list(map(lambda x: x ** 2, angka))

print(pangkat2)

pangkat3 = [i ** 2 for i in angka]  # list comprehension

print(pangkat3)

a = [1, 2, 3, 4, 5]
b = [2, 4, 8, 9, 56]

irisan = []

for i in a:
    for j in b:
        if i == j:
            irisan.append(i)

print(irisan)

irisan2 = [i for i in a for j in b if i == j]
print(irisan2)

# Latihan
'''
buah = ["mangga", "apel", "jeruk", "anggur", "semangka", "pisang"]
isi = ["coklat", "susu", "keju", "anggur", "pisang"]

Gunakan List Comprehension untuk membuat kombinasi buah dan isi, Tidak ada buah dan isi sama
[("mangga", "coklat"), ("apel", "coklat"), ("jeruk", "coklat").......]

("anggur", "anggur"), ("pisang", "pisang") ==> Tidak ada
'''
A = [1, 2]
B = ["a", "b", "c", "d"]

# Basic Syntax :
# zip(data_iterable 1, data_iterable 2)
# menghasilkan tipe data Object sehingga perlu dikonversi => Data iterable
zip_A = list(zip(A, B))
zip_B = tuple(zip(A, B))
zip_C = dict(zip(A, B))
print(zip_A)
print(zip_B)
print(zip_C)

list_1, list_2 = zip(*zip_A)
print(list_1)
print(list_2)

== == == == =

- Ketika awal di Run
akan keluar menu
MENU
1. REGISTER
2. LOGIN

-- REGISTER - -
Masukkan Data:
User ID: .... (Harus kombinasi huruf dan angka minimal 6 karakter) dan lakukan Pengecekan Duplikasi, Tidak boleh ada ID yg sama
Password: ... (harus kombinasi Huruf Kapital, Huruf kecil, dan angka minimal 8 karakter)
Email: .... (lakukan verifikasi email) == > Ketentuan Valid sesuai tugas sebelumnya = > Tidak boleh ada Email yg sama

Nama: ...
Gender: ...
Usia: ...
Pekerjaan: ...
Hobi: ... (Isi lebih dari satu)
Alamat:
    Nama Kota:
    RT:
    RW:
    Zip Code:
    Geo: Latitude - Longitude
No HP: ..... (harus 11-13 digit)

Simpan Data(Y/N)
Y: Data tersimpan
N: Data Tidak tersimpan

Setelah ini(Baik Y/N) akan kembali ke menu awal
-Register
-Login


--- LOGIN - --
Masukkan ID:
Masukkan Password:
Lakukan pengecekan ID dan password(Sesuai dengan kombinasi)
Notif:
- ID & Password Salah
- Password Salah
- ID Tidak Terdaftar
- Anda Berhasil Login


----MENU UTAMA---
1. Data Personal(User Profile)
Data Anda: Username
Nama:
Email:
Gender:
Usia:
Pekerjaan:
Hobi:
Alamat:
    Nama Kota:
    RT:
    RW:
    Zip Code:
    Geo: Latitude - Longitude
No HP:
2. Kalkulator
3. Konversi Romawi
4. Konversi Kode Morse
5. Hitung Hari(Masukkan Hari: senin, masukkan angka: 2) output = > Rabu
6. Kamus Hari == > Atau Project Bebas
7. Manipulasi Karakter == > Project Bebas
8. Konversi Jumlah Hari = > masukkan angka 14: output: 00 tahun 00 bulan 02 minggu 00 hari
9. Nilai Faktorial
10. Jumlah dan Deret Fibonacci == > User input angka: 7 = > output: Jumlah 7 deret pertama baris fibonacci, dan keluarkan deretnya
11. Data User == > Keluarkan hanya: Email, Username, Password
12. Menu CRUD: (Mini Aplikasi)
- Gunakan Dictionary:
**Contoh
Nama Barang - Stok = > Gudang
Nama Barang - Harga = > Toko/Kasir
Nama Karyawan - Gaji = > Penggajian
Nama Mahasiswa - Nilai = > Kampus
13. Exit

**Optional: Boleh tambahkan Sub menu lain
**Coba Gunakan Function: def, lambda, map, filter, dll sesuai dg kondisi dan kebutuhan

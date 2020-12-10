## input() ==> Agar prog. dapat menerima inputan dari user

Nama = str(input("Masukkan Nama : "))
Nama = input("Masukkan Nama : ")

85
'85'
# usia = float(input("Masukkan usia : "))
# # print(Nama)
# print(int(usia))
# print(type(usia))
Tipe data hasil dari inputan Semuanya STRING

Nama = "joni andre"
Name = "MIKE WINCHESTER"
usia = 25

# print(Nama.capitalize()) ## Mengubah Huruf pertama menjadi kapital
# print(Nama.title()) ## Mengubah huruf pertama untuk setiap Kata menjadi Kapital
# print(Name.lower()) ## Mengubah seluruh huruf menjadi Lower Case
# print(Nama.upper()) ## Mengubah seluruh huruf menjadi Upper case (Kapital)

# Alt 1
# print("Nama saya adalah", Nama) ## mengambil Value dari Variabel
# print("Nama saya adalah", Nama, "Dan berusia", usia)

# Alt 2 (Seluruh Variabel dalam bentuk String)
# print("Nama saya adalah " + Nama)

# print("Nama saya adalah " + Nama + " Dan berusia " + str(usia))


tahun = .....
if len(str(tahun)) == 1:
    hasilTahun = str(0) + str(tahun)
else:
    hasilTahun = str(tahun)
# print(Nama + Name) ## Concat => Penggabungan beberapa string
# print(Nama * 3) ## String akan ditampilkan sebanyak value INteger

# ## Kita dapat menggunakan Operator Matematika pada String, tapi terbatas pada + dan *
# + hanya dapat digunakan untuk data STRING dan STRING
# * hanya dapat digunakan untuk data STRING dan INTEGER


#Alt 3
# print("Nama Saya adalah {0} dan berusia {1}".format(Nama, usia))


#Alt 4
# print(f"Nama Saya adalah {Nama} dan berusia {usia}")

### Operator Matematika
# print(5 + 10)
# print(10 - 7)
# print(5 * 4)
# print(10 / 2)  ## Semua hasil pembagian menggunakan /, hasilnya bertipe FLOAT, meskipun hasilnya bil. bulat
# print(10 / 3)

# print(10 // 2)
# print(10 // 3) ## Akan menghasilkan bilangan Integer, dan nilai desimal akan diabaikan == Pembulatan kebawah

# print(10 % 7)  ## Modulus = Sisa hasil Bagi
# print(10 % 8)
# print(10 % 4)

# Basic Syntax : round(angka, jumlah desimal) Untuk Pembulatan, jika jumlah angka desimal tidak ditentukan, berarti NOL
# print(type(round(2.856932)))
Data yg dibulatkan menggunakan ROUND hingga tidak memiliki angka desimal, tipe data berubah menjadi Integer 

print(round(2.5)) ## Jika angka Depan adalah Genap, akan dibulatkan kebawah
print(round(3.5)) ## Jika angka depan adalah ganjil, akan dibulatkan keatas

# 1. 
# Joni memelihara ayam dan kambing, jumlah ayam dan kambing joni 13,
# jumlah kaki ayam dan kambing joni 32
# Berapa jumlah ayam dan kambing Joni?

# Input : 
# - Masukkan Jumlah Ayam dan Kambing :
# - Masukkan Jumlah Kaki ayam dan kambing : 

# Output :
# Jumlah Ayam joni ... ekor dan jumlah kambing joni ... ekor

# 2.
# Sembilan belas tahun lalu, umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya.
# Berapa usia Ibu saat melahirkan anaknya?

# Output nya :
# Usia Ibu ketika melahirkan anaknya adalah ... tahun

# 3. 
# Jumlah usia budi dan ayahnya sekarang adalah 50 tahun.
# 4 tahun lalu, usia ayah budi 6 kali usia budi 
2 - 40
# berapa usia ayah dan usia budi saat ini?
# Output nya :
# Usia ayah saat ini adalah ... tahun dan usia budi saat ini adalah .. tahun

# Kirim Email : (dalam bentuk file python .py)
khumaeni@purwadhika.com


# ---Library - Package - Module ----
# - Suatu Program yg telah dibuat oleh anggota komunitas baik individu maupun kelompok
# - Ada beberapa package/library yg sudah secara default terinstall dalam Python (Built in Package)
# - Beberapa Package/Library yg belum ada, ketika kita akan menggunakan, perlu melakukan instalasi terlebih dahulu

# Cara Menggunakan Package
#Alt 1
# import math ### Math adalah nama Library (Built in Package)
# # pi, floor, pow, ceil, sqrt ==> fungsi yg ada di dalam package/Library Math
# print(math.pi)  ## Menampilkan nilai pi
# print(math.pow(2, 3)) ## menampilkan Pangkat 
# print(math.floor(4.6)) ## Pembulatan kebawah
# print(math.ceil(2.3)) ## Pembulatan keatas
# print(math.sqrt(36)) ## Akar kuadrat

# ## Cara menggunakan Fungsi di dalam Package/Lib
# # Package.NamaFungsi()
# print("=" * 100)
# #Alt 2
# import math as m # memberikan nama alias untuk Package
# print(m.pi)
# print(m.pow(5, 2))
# print(m.floor(5.9))
# print(m.ceil(7.1))
# print(m.sqrt(16))
# print("=" * 50)
# #Alt 3
# from math import floor, ceil, pow

# print(floor(5.8))
# print(ceil(3.2))
# print(pow(3,3))

# nama = "Joni"
# usia = "25"
# print(nama.isalnum()) ## Mengandung - Seluruhnya adalah Alfa numerik
# print(usia.isdigit()) ## Apakah Seluruh elemen adalah Digit/Angka
# print(usia.isalpha()) ## Apakah seluruh elemen adalah Alfabet
# print(nama.islower()) ## untuk mengecek apakah seluruh elemen lower case
# print(nama.isupper()) ## untuk mengecek apakah seluruh elemen Upper case
# CRUD - Create, Read, Update, Delete 
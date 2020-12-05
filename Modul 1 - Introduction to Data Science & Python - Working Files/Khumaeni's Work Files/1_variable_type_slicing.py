# Interpreter ==> 
# def 
# (self, parameter_list):
#     """
#     docstring
#     """
#     pass
# compiler ==> C/Java/C++

# ## Python
# - Interpreter Programming Language => Program akan langsung mengeksekusi setiap baris Code dari atas kebawah
# - Case Sensitive ==> 'A' berbeda dengan 'a'
# - Tidak membutuhkan semicolon (;)
# - Tabulasi - Indentasi : memiliki fungsi penanda suatu Blok Kode


# untuk mengeluarkan/menampilkan hasil code ke dalam layar
# gunakan perintah    print(data)
# print(6+5)

# ## Beberapa tipe data dalam python
# ### Tipe Data Primitif ==> Tipe data dasar
# - String => Alfanumerik
# - Integer => Bilangan Bulat (dari negatif, nol dan positif)
# - Float => Bilangan Desimal
# - Complex Number ==> Jarang digunakan di Data Science ==> Bilangan Imajiner
# - Boolean => True dan False 



# ini adalah paragraf :
# ini pertemuan pertama

# def hitung():
# pass

### String
# print('halo')
# print("hari")
# print('''nama''')

# # print('hari ini adalah hari jum'at')  ### Keluar Error

# #Alt 1
# print('hari ini adalah hari jum"at')

# #Alt 2
# print("hari ini adalah hari jum'at")

# #Alt 3
# print('hari ini adalah hari jum\'at')

# print('''Halo selamat Pagi,
# hari ini hari selasa''')  ##digunakan ketika akan menampilkan string lebih dari 1 baris (Multiple Line)

### Integer
# print(56)
# print(9 + 9)
# print('9' + '9')

# # print('john' + ' pantau')

# # print(-8)
# print(9)
# print(type(9))
# print('9')
# print(type('9'))

# ## fungsi type(data) ==> digunakan untuk mengetahui Tipe Data

# ### Float => Bilangan Desimal
# print(5.6)
# print(type(5.6))

# ### Boolean
# print(True)
# print(type(True))


# #### Variabel 
# - Suatu tempat penyimpanan data yg diberi nama
# - Case sensitive 
# - Tidak bisa diawali dg number 
# - Tidak bisa ada spasi 
# - Tidak bisa menggunakan Reserved Words (Kata yg sudah ada fungsinya dalam python )
# - Tidak perlu mendeklarasikan/menentukan Tipe Data untuk variabel
 
#  ## Assignment Operator =
#  kotak dan data
#  kotak = data 
#  Kiri = Kanan ## Memasukkan Data disebelah kanan ke dalam variabel disebelah Kiri
# int angka = 25
# angka = 25
# 1 => Single Assignment
# rumusLuasPersegi = sisi * sisi


# a = 15  ### a,b,c,d adalah Variabel, dan 15, 20, nama saya, 6.05 adalah value yg kita masukkan kedalam variabel
# b = 20
# c = "Nama saya"
# d = 6.05

# print(a)
# print(b)
# print(c)
# print(d)

# #2 => Multiple Assignment
a, b, c = 50, 70, 90, 120, 150
# print(a)
# print(b)
a = 50, 70, 90

a, b = "John", "Bandung"

# print(a)
# print(b)

a = 25
b = 75
# print(a)
#kita akan menukar nilai, a menjadi 75 dan b menjadi 25
a, b = b, a
# a = b 
# b = a

# print(a)
# print(b)
# print(a)

# a = 45
# b = 45
# c = 45

a = b = c = 45
# print(a)
# print(b)
# print(c)

nama = "Joni Andre"
# J = 0
# o = 1
# n = 2
# i = 3
#  = 4
# A = 5
# n = 6
# d = 7
# r = 8
# e = 9
# Akses String dg Indexing
# Indexing di dalam python dimulai dari NOL
# akses index menggunakan kurung siku [ ]
## namaVariabel[indexnya]
# print(nama[0])
# print(nama[8])
# print(nama[9])

## Slicing - Subsetting

# - Kita mengakses beberapa elemen sekaligus 
# Basic Syntax :
# namaVar[start : end : step]
# print(nama[0:9:2])
# start : awal akses indexing 
# end : akhir AKSES indexing 
# step : langkah ketika mengakses 
# [Start : End] # Ketika Step tidak ditentukan, Default nya = 1
# [Inclusive : Exclusive]
# # Inclusive : Index tersebut ikut di akses 
# # Excusive : Akses sampai dengan Sebelum Index yg ditentukan (end - 1)
# print(nama)
# print(nama[0:3]) # 0 = Start (Inclusive), 3 = End (Exclusive), Step = Default = 1

# # Kita akan mengakses sampai Index terakhir
# #Alt 1
# print(nama[0:10])

# #Alt 2
# print(nama[0:]) # jika End atau Start dikosongkan, berarti akses dari paling awal atau Paling akhir

# print(nama[:3])

# print(nama[:]) # akan mengakses value dari paling awal sampai paling akhir

nama = "Joni Andre"

# print(nama[-1])
# print(nama[-5])
# print(nama[-10])
# print(nama[0])

# Menghitung panjang karakter dari String
# menggunakan fungsi len()
print(len(nama))

print(nama[::-1])

## Fungsi untuk mengubah Tipe Data
# int(data) # untuk mengubah data menjadi integer
# str(data) # untuk mengubah data menjadi string
# float(data) # untuk mengubah data menjadi float
## Notes : Data Harus sesuai
angka = int('9')

print(angka + angka)

bil = str(9)

print(bil + bil)

hari = int(5.8)
print(hari)

nilai = float('7')
print(nilai)

# val = int('5.8')
# print(val)

val2 = float('5.8')
print(val2)
# Nama = "Andi F Noya"
# angka = 10
# if angka%2 == 0:
#     print("Genap")
# else:
#     print("Ganjil")



# angka2 = 18
# if angka%2 == 0:
#     print("Genap")
# else:
#     print("Ganjil")


# angka3 = 20
# if angka%2 == 0:
#     print("Genap")
# else:
#     print("Ganjil")

# ====================def Function ==============

## Memberikan Nama Untuk suatu Fungsi, agar Fungsi dapat digunakan berkali-kali, tanpa perlu ketik ulang
## Memiliki Konsep yg sama dg Variabel, hanya saja kalau Variabel menyimpan data, kalau def menyimpan Fungsi
## Digunakan untuk Fungsi yg sifatnya Generik - Umum - yg akan dipake berkali-kali
## Jika Fungsi hanya digunakan sekali, sebaiknya tidak menggunakan Def Function


# angka = 10
# Basic Syntax :

# def NamFunction(Argumen):
#     Fungsi/Program nya

# Pemberian nama Function mengikuti aturan Penamaan Variabel
# Argumen - Bersifat Optional, Bisa kosong, Bisa berisi== Jumlah argumen tidak dibatasi => Tak terhingga



# CekBil(50)

# def CekBil(angka):
#     if angka%2 == 0:
#         print("Genap")
#     else:
#         print("Ganjil")

# CekBil(2)

## Inisialisasi Function
def NamaBuah():
    print("Ini Buah Jeruk")

## Cara Menggunakan Function - Memanggil Function
# NamaBuah()

# NamaBuah()

# NamaBuah()


def HargaBuah():
    NamaBuah()
    print("Harga Jeruk per kilo Rp.65.000")

# HargaBuah()

# kg = int(input("Masukkan Berat Buah : "))

## Argumen == Variabel
'''
Global Variabel ==> Variabel yg di define di Luar Function 
- Bisa digunakan di semua Tempat

Local Variabel ==> Variabel yg di define dan digunakan Di Dalam Function 
- Hanya dapat digunakan di dalam FUNCTION ybs (tempat var di define)
'''
A = 2 ## Global Variabel

def TotalBelanjaA():
    HargaBuah()

    harga = 65000 ## Local Var
    Total = A * harga ## Local Var
    print(A)
    print(harga)
    print(f"harga jeruk {A} Kilo adalah {Total}")

# TotalBelanja()

# print(A)
# print(harga)



# angka = 5
# hasil = angka * 10

###### Argumen
## Argumen = Local Variabel, tetapi Value nya Kita yg tentukan dari Luar Function
## Memasukkan Value-Data Ke dalam Local variabel
## Argumen di dalam function memiliki Fungsi sebagai Local Variabel

## Single Argumen
def TotalBelanja(Berat):
    # HargaBuah()
    # Berat = 5
    harga = 65000 ## Local Var
    Total = Berat * harga ## Local Var
    print(f"harga jeruk {Berat} Kilo adalah {Total}")


# TotalBelanja(5)

# TotalBelanja(10)

# TotalBelanja(4)

### Multiple Argumen
def guru(nama, pelajaran):
    # nama = ["Boni", "Beni"]
    # for i in nama:
    #     print(i)
    # pelajaran = ["Math", "Fisika"]
    print(f"Nama guru ini adalah {nama}")
    print(f"Mengajar Pelajaran {pelajaran}")

# guru("Roni", "Sejarah")
# guru("Ekonomi", "Susi")  ### Hasilnya akan salah, urutan memasukkan value,
# harus sesuai dengan urutan pada Argumen
# guru("Sandy") ### Jumlah value Harus sama persis dengan Jumlah Argumen pada Function
# guru("Math") ## Akan Error, karena Argumen ada 2, sedangkan Value yg dimasukkan hanya 1

# guru(["Boni", "Beni"], ["Math", "Fisika"])

#### Memanfaatkan Keywords
# guru(pelajaran='fisika', nama='Beni') 
## Langsung memasukkan value ke dalam argumen
# guru(nama='Boni', pelajaran='math')
# guru(nama="Fifi") ## Akan tetap error, meskipun menggunakan Keywords

### Menggunakan Nilai Default
# Kita menentukan - mendefine value dari argumen di dalam function
# GAJI = 7000000
# JOB = "staff"
jabatan = "Manajer"
gaji = 80000000
def pegawai(nama, jabatan="staff", gaji=7000000): ## staff dan 7000000 => Nilai Default
    print(f"Nama pegawai : {nama}")
    print(f"memiliki jabatan : {jabatan}")
    print(f"dan memiliki gaji : {gaji}")

# jabatan = "Manajer"
# gaji = 80000000
# pegawai(nama="Doni", jabatan="Data Manager", gaji=50000000)

# pegawai(jabatan="Staff IT", nama="Sisi")
# pegawai(nama="Lani")
# pegawai("Cecil")

# pegawai(jabatan="IT manager", gaji=60000000) # Akan Error, dan meminta Value untuk nama
# Karena Nama tidak kita masukkan Default Value nya
# Jika Argumen tidak ditentukan Default Value nya, Maka Wajib kita masukkan Value nya


### Return Function
# Function dengan Return Value
# Ketika kita hanya ingin mendapatkan Hasil dari Proses Fungsi/Program di dalam Function
# Dengan menggunakan Return Func. Kita bisa memasukkan Hasil Function ke dalam Variabel
# sehingga dapat digunakan untuk Kalkulasi lanjutan

def kuadrat(x):
    hasil = x ** 2
    return hasil

A = kuadrat(5) * 10
hasil = 500

# print(A)
def kuadrat2(x):
    hasil = x ** 2 ## Global Var, Value nya diupdate
    print(hasil) ## Var yg valuenya diupdate, merupakan Local Var


# kuadrat2(10) ## yg diambil adalah Local Var
# print(hasil)  ## yg diakses adalah Global Var

var1 = 20
var2 = 4

def pangkat(x = var1, y = var2):
    hasil = x ** y
    return hasil  ### Penentuan Variabel yg akan direturn sangat Penting

# C = pangkat(2,3)

# D = pangkat(4, 2)
# print(C)
# print(D)
'''
angka1 = int(input("Masukkan angka 1 : "))
angka2 = int(input("Masukkan angka 2 : "))

result = pangkat(angka1, angka2)
result2 = pangkat(x = angka1)
print(f"Hasil dari {angka1} pangkat {angka2} adalah {result}")
print(f"Hasil dari {angka1} pangkat var Global adalah {result2}")

'''

def perkalian(x, y):
    hasil = x * y
    return hasil

A = kuadrat(5)
B = pangkat(4,2)
print(A)
print(B)

C = perkalian(A, B)
print(C)


print(perkalian(kuadrat(5), pangkat(4,2)))

Latihan :
Email Verification-Validation

- Buat Sebuah Return Function dengan 1 Argumen untuk mengecek/Mevalidasi Email 

Input : Masukkan Email :

Kondisi :
Email Valid Jika :
- Memiliki format Nama User@nama hosting.ekstensi
- Nama user hanya boleh huruf, angka, underscore(_) dan dot(.)
- Nama Hosting hanya boleh Huruf dan Angka 
- Nama Ekstensi hanya boleh Huruf dan maksimal 5 karakter 

Output :
Alamat Email yang anda masukkan Valid !!

Jika Tidak Valid, Keluar Alasannya :
- Format Email Salah (Misal tidak ada @ atau tidak ada .ekstensi)
- Format Username yang anda masukkan salah
- Format Hosting yang anda masukkan salah
- Format Ekstensi yang anda masukkan salah

Contoh Email 
Valid :
andre@gmail.com 
joni_12@yahoo.com 
andy34@city.id 
steve.roger_77@avengers01.space

InValid :
andre254@gmail 
andre%^&@gmail.com 
john_capt@yah^^oo.com 
tony_stark@stark.corporation
Thor@@gmail.com



CekEmail(email)
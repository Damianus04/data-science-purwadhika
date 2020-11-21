## Looping

# While Looping 
# For Looping ===> 

# Looping memiliki karakter yg mirip dengan IF 
# karena sama-sama membutuhkan Conditional Statement (Kondisi yg bernilai TRUE atau FALSE)
# IF ==> Program akan dijalankan hanya SATU kali (Kondisi Bernilai TRUE)
# Looping ==> Program akan dijalankan beberapa kali/berulang kali/Beberapa iterasi (Selama Kondisi Bernilai TRUE)

# Looping digunakan => Ketika kita ingin Menjalankan Program yg sama berulang kali 

# - Jenis Looping :
# While Loop
# For Loop 

# Basic Syntax :
# While ....Kondisi (Conditional Statement)...: Selama Kondisi Bernilai TRUE, Program akan dijalankan.
#     ... Program...

# angka = 1 ## Define Variabel yg akan dilakukan Pengecekan Kondisi
# while angka < 10:  ## Proses Looping akan dihentikan, ketika Kondisi Bernilai FALSE
#     # angka = angka + 1
#     print(angka)
#     angka = angka + 1 ## Increment => Penambahan 1, kita lakukan Manual
# iterasi = 1  ### Untuk While, harus mendefine Kondisi Awal (Inisiasi Looping) (Variabel)
# while iterasi < 11:
#     print("Selamat Datang")
#     iterasi += 1  ### Buat Increment/Decrement Manual => Penambahan Maupun Pengurangan
# print("Selamat Datang")


angka = 5  ## Diperlukan untuk memulai Looping
while angka > 0:
    print((str(angka) + " ") * angka)
    angka -= 1 ## Diperlukan untuk menghentikan Looping

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
+ dan *
Inisiasi awal 
Iterasi ke-1 : angka = 5
- pengecekan kondisi While (karena TRUE, program akan dijalankan)

'5 ' * 5
5 5 5 5 5 

- Masuk ke Decrement Manual 
angka = 5 - 1
angka = 4

Iterasi ke-2 : angka = 4 
- Pengecekan kondisi While (Karena TRUE, Program akan dijalankan)
'4 ' * 4
4 4 4 4 
- masuk ke Decrement Manual 
angka = 4 - 1
angka = 3

Iterasi ke-3 : angka = 3 
- Pengecekan kondisi While (Karena TRUE, Program akan dijalankan)
'3 ' * 3
3 3 3 
- masuk ke Decrement Manual 
angka = 3 - 1
angka = 2

Iterasi ke-4 : angka = 2
- Pengecekan kondisi While (Karena TRUE, Program akan dijalankan)
'2 ' * 2
2 2 
- masuk ke Decrement Manual 
angka = 2 - 1
angka = 1

Iterasi ke-5 : angka = 1
- Pengecekan kondisi While (Karena TRUE, Program akan dijalankan)
'1 ' * 1
1 
- masuk ke Decrement Manual 
angka = 1 - 1
angka = 0

Iterasi ke-6 : angka = 0
- Pengecekan kondisi While (Kondisi Bernilai FALSE, maka Looping akan dihentikan)
'''
# # Tahapan Looping => Iterasi => Iterable Object
# Iterasi ke-1 : angka = 1
# print 1

# Iterasi ke-2 : angka = 2
# print 2

# Iterasi ke-3 : angka = 3
# print 3
# ....
# ....

# Iterasi ke-8 : angka = 8
# print 8

# Iterasi ke-9 : angka = 9
# print 9 
# Iterasi ke-10 : angka = 10
'''
################# Tebak Angka
'''
angka = 598
tebak = "angka awal"

while tebak != angka:
    tebak = int(input("Masukkan Angka : "))
    if tebak == angka:
        print("Tebakan Berhasil")
    elif tebak > angka:
        print("Angka Lebih kecil dari Tebakan Anda")
    else:
        print("Angka Lebih Besar dari Tebakan Anda")
'''
# Menu Aplikasi ...
# ...
# ...
# ...
# ...
# 5 Exit 
'''
password = "andi1234"
Login = ""
coba = 1
batas_coba = 3

while Login != password and coba <= batas_coba:
    if coba <= batas_coba:
        Login = input("Masukkan Password Anda : ")
        if Login != password and coba < batas_coba:
            coba += 1
            print(f"Password Salah, Silakan coba Lagi: percobaan ke-{coba}")
        elif Login != password and coba == batas_coba:
            coba += 1
            print(f"Password Salah, dan Kesempatan Habis")
        else:
            print("Password Benar, Anda Berhasil Login")
            # print(Menu)

Lat :
Soal 1
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Soal 2
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
'''
##### FOR Loop
- Pada For Loop dapat dilakukan Increment/Decrement secara Otomatis
- Inisiasi Awal Looping Tidak harus mendefine Variabel   


Basic Syntax 
for ...Variabel... in ... Iterable Object/Data...: ### Looping akan dijalankan hingga Seluruh Data Iterable diakses
    ...Program... ## Program akan dijalankan Selama Data Iterable Diakses (Kondisi TRUE)

Iterable Object/Data ==> Data/Object yg isinya Lebih dari 1 ==> Sebagian besar dapat dilakukan Indexing 
'''
# for i t in angka:
#     print(i)
#     for j in angka:
#         print(j)
#         for k in angka:
#             print(k)
'''
angka = range(10)
print(angka)

Range Mirip dg indexing dan Berisi Angka/Numerik
Angka berupa Integer

range(START, END, STEP)

range(10) ### Ketika di dalam Range, angka hanya 1, Angka tersebut adalah STOP
## Default START = 0
## DEFAULT STEP = 1  ==> Secara Default berarti PENAMBAHAN 1 ==> Increment Otomatis

range(1, 10)  ### Ketika di dalam Range angka hanya 2, Angka tersebut adalah START dan STOP
## Default STEP = 1
Mengikuti Aturan Inclusive dan Exclusive
START = Inclusive 
END = Exclusive = Akses akan berhenti sampai di END - 1

range(1, 21, 2) ### START = 1, END = 21 (Akses akan berhenti di 21-1 = 20), STEP = 2 (Penambahan Otomatis 2)

range(20, 1, -1)
'''
'''
# i = 5
for i in range(10):  ### Tidak perlu inisiasi Awal
    print(i) ## Increment dilakukan Otomatis

## in ==> Membership Operator Menghasilkan TRUE dan FALSE

print('=' * 50)

# i = 0
# while i < 10:
#     print(i)
    # i += 1
for i in range(3, 10):
    print(i)

- For secara natural dengan sendirinya bisa Mendapatkan Kondisi False (Menghentikan Proses Looping) == Limited Looping
- While tidak bisa mendapatkan Kondisi False kecuali Kita tentukan ==> Bisa Unlimited Looping

print('=' * 50)

i = 0
while i in range(10):
    print(i)
    i += 1

print('=' * 50)
for i in range(1, 21, 2): ### Ketika STEP Increment, Exclusive (END - 1)
    print(i)

print('=' * 50)
for i in range(10, 0, -1): ## Ketika STEP Decrement, Exclusive (END + 1)
    print(i)
'''

### Syntax Tambahan Dalam Looping
########## BREAK ===> Untuk Menghentikan Proses Looping Secara PAKSA
# Secara Normal/Natural ==> Looping akan Berhenti Ketika Kondisi Bernilai FALSE 
## Break Biasanya dipasangkan dengan IF Statement
'''
for i in range(10):
    print(i)

print('=' * 50)

for i in range(10): ### Iterasi ketika i = 5
    print(i) # print 5
    if i == 5:
        break # Looping dihentikan

print('=' * 50)

for i in range(10): ### Iterasi ketika i = 5
    if i == 5:
        break # Looping dihentikan
    print(i)


hari = 'Selasa'

for i in hari:
    print(i)

print('=' * 25)

i = 0
while i < len(hari):
    print(hari[i])
    i += 1
'''
'''
##### Continue
### Continue biasanya dipasangkan dg IF Statement
### Menghentikan Sementara Proses Looping (Tahapan-Iterasi) langsung ke
### Iterasi berikutnya
for i in range(10):
    print(i)

print('=' * 50)
for i in range(10): ### Iterasi ketika i = 5
    print(i)
    if i == 5:
        break # Looping dihentikan

print('=' * 50)
for i in range(10): ### Iterasi ketika i = 5
    print(i)
    if i == 5:
        continue # Looping dihentikan dan langsung menuju Iterasi berikutnya

print('=' * 50)
for i in range(10): ### Iterasi ketika i = 5
    if i == 5:
        continue
    print(i) ## Ketika i = 5 akan di SKIP, lanjut iterasi berikutnya
    # print(f"Ini adalah angka ke {i}")## Ketika i = 5 akan di SKIP, lanjut iterasi berikutnya
'''

### BREAK ==> Proses Looping secara keseluruhan Dihentikan Secara PAKSA
### Continue ==> Tahapan - Iterasi dari Looping Dihentikan, kemudian Lanjut iterasi berikutnya

###### ELSE
# Perintah/Program Dibawah Else akan DIjalankan Ketika Looping Berhenti Secara NATURAL
# Biasanya dipasangkan dengan BREAK

angka = 5
for i in range(20):
    print(i)
    if i == angka:
        print("Data Ditemukan")
        continue
    # else:
#     #     print("Data Tidak Ditemukan!!!!!!!!!!")
else:
    print("Data Tidak Ditemukan")
# print("Data Tidak Ditemukan")
print("Perintah/Program Di Luar Looping")

Tugas :
Soal 1                              Soal 4                                  Soal 7
1                                   1 1 1 1 1                                   *
2 2                                 2 2 2 2                                   * * *
3 3 3                               3 3 3                                   * * * * *
4 4 4 4                             4 4                                   * * * * * * *
5 5 5 5 5                           5                                   * * * * * * * * *
                                                                        * * * * * * * * *
Soal 2                              Soal 5                                * * * * * * * 
1                                   1 2 3 4 5                               * * * * *
1 2                                 1 2 3 4                                   * * *
1 2 3                               1 2 3                                       *
1 2 3 4                             1 2
1 2 3 4 5                           1

Soal 3                              Soal 6
5                                   5 4 3 2 1
5 4                                 5 4 3 2
5 4 3                               5 4 3
5 4 3 2                             5 4
5 4 3 2 1                           5

Kirim email : khumaeni@purwadhika.com
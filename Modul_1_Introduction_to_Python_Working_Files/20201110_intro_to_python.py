#

# # Case 1
# x, y, z = 4, 3, 2
# w = (((x+y) * z)/(x*y)) ** 2

# print(w)
# print()

# # Case 2
# number = int(input("please input a number: "))
# result = number ** 2
# print("square of", number, "is", result)
# print()


# Case 3
# days = int(input("please input number of days: "))
# n_year = 360
# n_month = 30
# n_week = 7


# year = int(days / 360)
# year_mod = days % 360
# month = int(year_mod / 30)
# month_mod = month / 30
# # week = int(month_mod / 4)
# # week_mod = week % 4
# day = int(month_mod % 7)

# print(year, "year,", month, "month,", day, "day.")


# Case 5
# text = str(input("please input your text: "))
# text_length = len(text)
# print("length of ", text, "is", text_length, "characters")

# Case 4

# Case 6


# 20201112 - FIRST TASK
# Task 1
# Joni memelihara ayam dan kambing, jumlah ayam dan kambing joni 13,
# jumlah kaki ayam dan kambing joni 32
# berapa jumlah ayam dan kambing joni

# Input:
# - masukkan jumlah ayam dan kambing
# - masukkan jumlah kaki ayam dan kambing

# Output:
# jumlah ayam joni ... ekor dan jumlah kambing joni ... ekor

# total_binatang = int(input("Jumlah ayam dan kambing: "))
# total_kaki = int(input("jumlah kaki ayam dan kambing: "))

# kaki_ayam = 2
# kaki_kambing = 4

# kambing = int((total_kaki - (2*total_binatang))/(kaki_kambing - kaki_ayam))
# ayam = int(total_binatang - kambing)

# print(f"jumlah ayam joni {ayam} ekor dan jumlah kambing joni {kambing} ekor")


# Task 2
# https://github.com/richardadinugraha/PythonFundamental/blob/master/2_Aritmatika.py
# 19 tahun lalu, umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya.
# Berapa usia Ibu saat melahirkan anaknya?

# Output:
# Usia Ibu ketika melahirkan anaknya adalah ... tahun

# periode_lalu = float(input("masukkan periode ke belakang: "))
# selisih_usia_1 = float(input("selisih usia pertama: "))
# rasio_1 = float(input("rasio pertama: "))
# rasio_2 = float(input("rasio kedua: "))
# selisih_usia_2 = float(input("selisih usia kedua: "))


# usia_ibu = int((28 * ((19/4) + selisih_usia_1))/3)
# usia_anak = int((usia_ibu/rasio_2) + selisih_usia_2)
# usia_ibu_melahirkan = int(usia_ibu - usia_anak)

# print(f"usia ibu ketika melahirkan anak adalah {usia_ibu_melahirkan} tahun")

# Task 3
# Jumlah usia budi dan ayahnya sekarang adalah 50 tahun.
# 4 tahun lalu, usia ayah budi 6 kali usia budi.
# berapa usia ayah dan usia budi saat ini?

# Output:
# Usia ayah saat ini adalah ... tahun dan usia budi saat ini adalah ... tahun

# total_usia = int(input("total_usia: "))
# rasio_usia = int(input("rasio usia: "))
# periode_lalu = int(input("masukkan periode ke belakang: "))


# # usia_budi = ""
# # usia_ayah = selisih_usia * usia_budi - 20
# usia_budi = int((total_usia + (rasio_usia * periode_lalu)) / 7)
# usia_ayah = int(total_usia - usia_budi)

# print(
# f"Usia ayah saat ini adalah {usia_ayah} tahun dan usia budi saat ini adalah {usia_budi} tahun")

# kirim email: khumaeni@purwadhika.com


# ===Operator Perbandingan

# Output = TRUE dan FALSE

# # == : sama dengan
# # != : Tidak sama dengan
# # < : kurang dari
# # > : lebih dari
# # <= : kurang dari sama dengan
# # >= : lebih dari sama dengan

# ===Operator Gabungan
# angka=30

# angka=angka + 5
# angka += 5

# angka=angka - 4
# angka -= 4

# angka=angka * 2
# angka *= 2

# angka=angka / 2
# angka /= 2

# pow(2, 3) == > 2 pangkat 3
# 2 ** 3 == > 2 pangkat 3

# angka=angka ** 2
# angka **= 2

# angka=angka % 7
# angka %= 7

# ===Operator membership
# in
# not in

# nama = "Nama saya joni andre dan tinggal di jakarta"
# print(nama.replace)("joni", "mike")
# print(nama.split(" "))
# print(nama.split(" ", 1))
# print(nama.split("dan"))
# print(nama.count('j'))


# 20201112 - SECOND TASK
# TASK 1
# Input: jumlah hari:
# output: ... tahun ... bulan .. minggu .. hari

# notes:
# 1 tahun = 365 hari
# 1 bulan = 30 hari

# days = int(input("please input number of days: "))
# n_year = 365
# n_month = 30
# n_week = 7

# year = days // n_year  # 35 hari
# days_mod = days % n_year
# print(days_mod)

# month = days_mod // n_month
# days_mod = days_mod % n_month
# print(days_mod)

# week = days_mod // n_week
# week_mod = days_mod % n_week
# print(days_mod)

# day = int(week_mod)

# print(year, "year,", month, "month,", week, "week", day, "day.")

# TASK 2
# Input:
# masukkan kalimat:
# masukkan karakter: x
# output:
# jumlah karakter x di dalam kalimat xxxx adalah 5

# Hari ini, HARI TidAKMasuk KuliAH
# masukkan karakter: a
# output: 5

# text = str(input("please input your text: "))
# character = str(input("character to count: ")).lower()

# lower_text = text.lower()
# result = lower_text.count(character)
# print("number of", character, "is", result, "characters")

# TASK 3
# Input:
# masukkan text: Hari ini adalah Hari Rabu
# masukkan huruf vokal: o
# output: Horo ono odoloh horo robo

# text = str(input("input your text: "))
# vocal_to_replace = str(input("type replacement character: ")).lower()
# vocal_characters = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]

# for character in vocal_characters:
#     if character in text:
#         text = text.replace(character, vocal_to_replace)

# print(text)


# TASK 4: BMI Calculator
# mass = float(input("input body mass: "))
# height = float(input("input body height: "))
# height_in_m = height/100
# IMT = mass / height_in_m ** 2

# Kondisi: nilai tinggi dan massa tidak boleh negatif =>  jika negatif maka keluar notifikasi "tidak menerima angka negatif"
# Kondisi: nilai tinggi dan massa tidak boleh string atau desimal => jika salah ada notif "angka yang anda masukkan salah"
# Batas maksimal massa: 200 kg dan tinggi 300 cm ==> jika lebih ada notif "tinggi / massa yang anda masukkan di luar batas"
# Output: sesuaikan dengan hasil
# BMI < 18.5 ==> berat badan kurang
# 18.5 - 24.9 ==> berat badan ideal
# 25 - 29.9 ==> berat badan berlebih
# 30 - 39.9 ==> bb sangat berlebih
# BMI >= 40 ==> obesitas

# Tinggi badan anda ... m dan massa anda ... kg, BMI anda ... dan anda termasuk ...

# try:
#     mass = float(input("input body mass: "))
#     height = float(input("input body height: "))

#     if (1 <= mass <= 200) and (1 <= height <= 300):
#         height_m = height/100
#         BMI = round(mass / height_m ** 2, 2)
#         BMI_status = "not calculated"

#         if 0 < BMI < 18.5:
#             BMI_status = "less ideal"
#         elif 18.5 <= BMI <= 24.9:
#             BMI_status = "ideal"
#         elif 25.0 <= BMI <= 29.9:
#             BMI_status = "overweight"
#         elif 30.0 <= BMI <= 39.9:
#             BMI_status = "very overweight"
#         elif BMI >= 40:
#             BMI_status = "obecity disorder"

#         print(
#             f"Your height is {height_m} m, your body mass is {mass}, your BMI is {BMI}, and you are {BMI_status}")
#     elif mass > 200:
#         print("body mass should be under 200 kg")
#     elif height > 300:
#         print("body height should be under 300 cm or 3 meter")
#     else:
#         print("mass and height cannot be lower than or similar to 1")

# except ValueError:
#     print("mass or weight must be number, cannot be string")
# except ZeroDivisionError:
#     print("zero division error, body mass and height cannot be lower than 1")


# TASK 5: Score value
# Input:
# Masukkan nilai: ...

# Kondisi:
# >90: Grade A
# >85: Grade A-
# >80: Grade B
# >75: Grade B-
# >70: Grade c
# >65: Grade D
# <65: Anda tidak lulus dan perlu remedial

# - nilai maksimum 100, nilai minimum 0
# - jika nilai > 100: nilai di luar jangkauan
# - jika nilai < 0: tidak menerima nilai negatif
# - jika input bukan angka: angka yang anda masukkan salah
# - bisa menerima nilai desimal

# output:
# nilai anda ... dan anda ... (sesuai kondisi)


# try:
#     score = float(input("input your score: "))
#     grade = "not defined"

#     if 0 <= score <= 100:
#         if 90 < score <= 100:
#             grade = "Grade A"
#         elif 85 < score <= 90:
#             grade = "Grade A-"
#         elif 80 < score <= 85:
#             grade = "Grade B+"
#         elif 75 < score <= 80:
#             grade = "Grade B-"
#         elif 70 < score <= 75:
#             grade = "Grade C"
#         elif 65 < score <= 70:
#             grade = "Grade D"
#         elif 0 <= score <= 65:
#             grade = "unqualified Grade"

#         print(f"your score is {score} and your grade is {grade}")
#     elif score > 100:
#         print("score cannot be greater than 100")
#     elif score < 0:
#         print("score cannot be lower than 0")

# except ValueError:
#     print("your input should be score number between 0 - 100")


# email ke khumaeni@purwadhika.co.id
# deadline: senin jam 12 siang


# IF STATEMENT

# Case 1: odd/even checker --> try and except fails
# number = int(input("input your number: "))

# try:
#     if number % 2 == 0:
#         print(f"{number} is even number")
#     else:
#         print(f"{number} is odd number")
# except:
#     print("input should be number")

# Case 2: IMT calculator
# mass = float(input("input body mass: "))
# height = float(input("input body height: "))
# height_in_m = height/100
# IMT = mass / height_in_m ** 2

# print(f"mass is {mass} kg and height is {height_in_m} m")

# if IMT < 18.5:
#     print(f"IMT is {IMT} your body is less ideal")
# elif 18.5 >= IMT <= 24.9:
#     print(f"IMT is {IMT} your body is ideal")
# elif 25.0 >= IMT <= 29.9:
#     print(f"IMT is {IMT} your body is overweight")
# elif 30.0 >= IMT <= 39.9:
#     print(f"IMT is {IMT} your body is very overweight")
# else:
#     print(f"IMT is {IMT} you have obecity disorder")


# ERROR & EXCEPTION HANDLING
# try:
#     inp = input()
#     print("Press ctrl+c or interrup the kernel")
# except KeyboardInterrupt:
#     print("Caught KeyboardInterrupt")
# else:
#     print('no exception occured')

# Zero division
# try:
#     a = 100/2
#     print(a)
# except ZeroDivisionError:
#     print("Zero division exception raised.")
# else:
#     print("success, no error")

# Key error
# try:
#     a = {1: 'a', 2: 'b', 3: 'c'}
#     print(a[3])
# except LookupError:
#     print("Key error exception raised")
# else:
#     print("success, no error")

# Value error
# try:
#     input = float(input('input number: '))
# except ValueError:
#     print("could not convert string to float")
# else:
#     print('success, no error')

# cek


# Looping
# while Looping
# for looping
# sama seperti if, looping bisa nested

# WHILE LOOP
# looping memiliki karakter yang mirip dengan IF
# karena sama-masa membutuhkan conditional statement (kondisi yang bernilai TRUE atau FALSE)
# IF => program akan dijalankan hanya SATU kali (Kondisi bernilai TRUE)
# Looping => program akan dijalankan beberapa kali/berulang kali/beberpa iterasi (selama kondisi bernilai TRUE)

# Looping digunakan => ketika ingin menjalankan program yang sama berulang kali

# x = 0
# while x < 10:
#     print(x)
#     x += 1

# angka = 1 # define variable yang akan dilakukan pengecekan kondisi
# while angka < 10: # proses looping akan dihentikan, ketika kondisi bernilai FALSE
#     print(angka)
#     angka = angka + 1 #increment => penambahan 1, kita lakukan manual

# # Tahapan looping => iterasi => iterable object
# iterasi ke-1: angka = 1
# print(1)

# iterasi ke-1: angka = 2
# print(2)

# iterasi ke-1: angka = 3
# print(3)
# ...
# ...

# iterasi ke-8: angka = 8
# print(8)

# iterasi ke-9: angka = 9
# print(9)

# iterasi ke-10: angka = 10

# Tebak Angka
# angka = 598
# tebak = ""

# while tebak != angka:
#     tebak = int(input("masukkan angka: "))
#     if tebak == angka:
#         print("Tebakan Berhasil")
#     elif tebak > angka:
#         print("Angka lebih kecil dari tebakan Anda")
#     else:
#         print("Angka lebih besar dari tebakan Anda")

'''
password = 'andi1234'
login = ""
coba = 1
batas_coba = 5

while login != password and coba <= batas_coba:
    if coba <= batas_coba:
        login = input("masukkan password Anda: ")
        if login != password and coba < batas_coba:
            coba += 1
            print(f"password Salah, silakan coba lagi. Percobaan ke-{coba}")
        elif login != password and coba == batas_coba:
            coba += 1
            print(f"password salah dan kesempatan habis")
        else:
            print("password benar, anda berhasil login")



iterasi = 1  # untuk while, harus mendefine kondisi awal (inisiasi looping)
while iterasi < 11:
    print('Selamat Datang')
    iterasi += 1  # buat increment/decrement manual -> penambahan atau pengurangan
print("Selamat Datang")

iterasi = 5
while iterasi > 0:
    print((str(iterasi) + " ") * iterasi)
    iterasi -= 1

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# inisiasi awal
# iterasi ke-1 : angka = 5
# - pengecekan kondisi while (karena TRUE, program akan dijalankan)

# '5 ' * 5
# 5 5 5 5 5

# = masuk ke decrement manual
# angka = 5 - 1
# angka = 4

# iterasi ke-2 : angka = 4
# - pengecekan kondisi while (karena TRUE, program akan dijalankan)

# '4 ' * 4
# 4 4 4 4

# = masuk ke decrement manual
# angka = 4 - 1
# angka = 3

# iterasi ke-3 : angka = 3
# - pengecekan kondisi while (karena TRUE, program akan dijalankan)

# '3 ' * 3
# 3 3 3

# = masuk ke decrement manual
# angka = 3 - 1
# angka = 2

# iterasi ke-4 : angka = 2
# - pengecekan kondisi while (karena TRUE, program akan dijalankan)

# '2 ' * 2
# 2 2

# = masuk ke decrement manual
# angka = 2 - 1
# angka = 1

# iterasi ke-5 : angka = 1
# - pengecekan kondisi while (karena TRUE, program akan dijalankan)

# '1 ' * 1
# 1

# = masuk ke decrement manual
# angka = 1 - 1
# angka = 0

# iterasi ke-6 : angka = 0
# - pengecekan kondisi while (karena FALSE, program akan berhenti)


# FOR LOOP
# increment/decrement pada for loop dapat terjadi otomatis
# inisiasi awal looping tidak harus men define variable

# Basic Syntax
# for ...variable... in ... iterable object/data...: #looping akan dijalankan hingga seluruh data iterable diakses
#     ...program... # program akan dijalankan selama data iterable diakses (TRUE)

# iterable object/data -> data/object yang isinya lebih dari 1 -> sebagian besar dapat dilakukan indexing

# for i in angka:
#     print(i)
#     for j in angka:
#         print(j)

# angka = range(10)
# print(angka)
# range mirip dengan indexing dan berisi angka/numerik
# angka berupa integer
# range(START, END, STEP)

# range(10) # ketika di dalam range, angka hanya 1, angka tersebut adalah STOP
# default START = 0
# default STEP = 1

# range(1, 10) # ketika di dalam range, angka hanya 2, angka tersebut adalah START dan STOP
# default START dan STOP mengikuti aturan inclusive & exclusive
# default STEP = 1

for i in range(10):
    print(i)

print('=' * 50)

for i in range(3, 10):
    print(i)


# for secara natural dengan sendirinya bisa mendapatkan kondisi false (menghentikan proses looping) == limited looping
# while tidak bisa mendapatkan kondisi false kecuali kita tentukan -> bisa unlimited looping
for i in range(1, 21, 2):  # ketika step increment, Exclusive (end - 1)
    print(i)

for i in range(10, 0, -1):  # ketika step decrement, Exclusive (end + 1)
    print(i)
'''

'''
# syntax tambahan dalam looping
# BREAK -> menghentikan proses looping secara paksa
for i in range(10):
    print(i)

print('='*50)

for i in range(10):
    print(i)
    if i == 7:
        break

hari = "Selasa"
for i in hari:
    print(i)

print("-"*50)
hari = "Selasa"
i = 0
while i < len(hari):
    print(hari[i])
    i += 1


# CONTINUE -. biasanya dipasangkan dengan if statement, menghentikan sementara proses looping (tahapan-iterasi langsung ke iterasi berikutnya)
for i in range(10):
    print(i)
    if i == 5:
        break

print("-"*50)
for i in range(10):
    if i == 5:
        continue  # ketika i = 5 akan di skip, lanjut ke iterasi berikutnya
    print(i)
    print(f"ini adalah angka ke {i}")


# ELSE
# perintah/program di bawah else akan dijalankan ketika looping berhenti secara natural
angka = 25
for i in range(20):
    print(i)
    if i == angka:
        print("Data ditemukan")
        break
    else:
        print("Data tidak ditemukan !!!!")

print("Perintah/program di luar looping")


# latihan 1
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# latihan 2a
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# latihan 2b
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# latihan 3
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# latihan 4
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# latihan 5
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# latihan 6
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# latihan 7
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# kirim email ke khumaeni@purwadhika.com

# 1
x = 0
while x < 5:
    x += 1
    x_string = str(x) + " "
    print(x_string * x)

print("-" * 100)

# 2
x = 6
y = 0
while x > 0:
    x -= 1
    y += 1
    y_string = str(y) + " "
    print(y_string * x)


# STRING
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
# print(hari.index('Kamis'))

print(hari[1:3])  # akan mengakses index 1 sampai dengan index 2 (end - 1)
print(hari[2:])  # akan mengakses index 2 sampai index terakhir (paling akhir)
print(hari[:4])  # akan mengakses index paling awal sampai index ke-3 (end-1)
print(hari[:])  # akan mengakses keseluruhan elemen, dengan STEP +1 (increment)
# akan mengakses keseluruhan elemen, dengan STEP -1 (decrement)
print(hari[::-1])


# menambahkan data dengan append dan extend
nama = ['andi', 'beni', 'doni']
# nilai = [89, 90, 78]

# nama.append(nilai)
# print(nama)
# nama.extend(nilai)
# print(nama)
hari.append('sunday')
print(hari)

# menambahkan data dengan insert
hari.insert(3, 'wednesday')
print(hari)

hari[1] = 'selasa 2'
print(hari)
'''

# menghapus data dengan remove


# from typing import Union
# hari = ["Senin", "Kamis", "Selasa", "Rabu",
#         "Kamis", "Jumat", "Sabtu", "Kamis", "Selasa"]
# print(hari)

# # hari.remove('Kamis')
# # print(hari)

# # hari.pop(4)
# # print(hari)

# for i in hari:
#     if i == "Kamis":
#         hari.remove("Kamis")
# print(hari)


# TASK ASSIGNMENT
'''
- kelompok 2 - 3 orang
- mini application
- CRUD - Create, Read, Update, Delete

aplikasi mini untuk data barang / elektronik / buah / atk / dll
1. apps awal di run - akan meminta login (password)
2. batas 4x
3. jika salah password sampai 4x akan keluar aplikasi

jika password benar: akan keluar menu

--Menu--
1. cetak isi daftar barang (read)
2. menambahkan data barang (create)
3. mengubah data barang (update)
4. menghapus data barang (delete)
5. exit (keluar apps)

--kondisi (T&C)
1. Read (cetak data)
- jika tidak ada data, akan keluar notif: daftar barang masih kosong
- jika ada data, akan menampilkan seluruh data barang

2. Create (tambah data)
- pengeceken jenis data, jika salah format: data yang anda masukkan salah
- pengecekan duplikasi:
jika data sudah ada sebelumnya, 
keluar notifikasi:
data sudah ada, apakah tetap akan disimpan? (Y/N)
Y: keluar notif - data tersimpan --> data akan disimpan
N: keluar notif - data tidak tersimpan
- ketika data berhasil disimpan, keluar notif: data berhasil disimpan (jika tidak ada duplikasi)

3. Update (ubah data)
- program akan meminta user memasukkan data yang akan diupdate
- jika data yang diminta user tidak ada, keluar notif: data barang tidak ada.
- jika barang ada -> update datanya -> jeruk - jeruk bali
- keluar notif: data terupdate/data berhasil diubah

4. Delete (hapus data)
- program akan meminta user memasukkan data yang akan dihapus
- jika data yang diminta user tidak ada keluar notif: data barang tidak ada
- jika barang ada -> hapus seluruh data yang sesuai dengan inputan user

5. Exit
- selama user belum memilih opsi ini, menu akan terus ditampilkan

setelah melakukan proses CRUD (akan keluar mini menu yang memiliki 2 opsi)
1. kembali ke menu utama
2. ke menu awal (yang diakses)

kirim ke email: khumaeni@purwadhika.com
deadline: Selasa
'''


# if input_item in car_list:
#                                 index = car_list.index(input_item)
#                                 if input_item == car_list[index]:
#                                     command = str(
#                                         input("\t\t---> Data has been registered.\n \t\tDo you want to add?(Y/N): ")).upper()
#                                     if command == "Y":
#                                         car_list.append(input_item)
#                                         print("\t\t'item has been added'")
#                                     else:
#                                         print("\t\t'item is not added'")
#                                     for n, i in enumerate(car_list):
#                                         print(f"\t\t{n+1}. {i}")
#                                 else:
#                                     print("data incorrect")


# elif input_item not in car_list:
#                                 command = str(
#                                     input("\t\t---> Data is not registered.\n \t\tDo you want to add data?(Y/N): ")).upper()
#                                 command = command.upper()
#                                 if command == "Y":
#                                     car_list.append(input_item)
#                                     print(f"\t\t'item has been added'")
#                                 else:
#                                     print("\t\t'item is not added'")
#                                 for n, i in enumerate(car_list):
#                                     print(f"\t\t{n+1}. {i}")


# 20201123
# TUGAS
# 1. Hari = ["senin", "selasa", "rabu", "kamis", "jum'at", 'sabtu', 'minggu']

# input:
# "masukkan nama Hari: " senin
# "masukkan jumlah: " 100 (nilai harus integer) - jika bukan integer keluar notifikasi: ..., bisa minus

# Output:
# " 100 hari dari (senin) ... adalah hari ..."
# " -2 hari dari (senin) ... adalah hari (sabtu)..."
# "3 hari dari hari (senin) ... adalah hari (kamis)..."

# kondisi:
# - tidak case sensitive
# - ada pengecekan hari: tidak ada nama hari
# - jumlah angka harus integer (bisa positif maupun negatif)

# 2. Palindrome
# katak = katak
# Level = level
# Madam = Madam
# Noon = Noon

# input: masukkan kata: ....
# kondisi: lakukan pengecekan apakah kata tersebut masuk palindrome

# output: kata ... tidak termasuk/palindrome

# 3. gunakan hanya fungsi numerik-aritmatik (+ - * / % //)
# input: masukkan 4 digit angka: 5493
# output: 9354 (2 digit belakang pindah ke depan)


# 4. gunakan hanya fungsi numerik-aritmatik (+ - * / % //)
# input:
# masukkan 2 digit angka: 63
# masukkan 2 digit angka kedua: 87

# output: 6387

# kondisi untuk soal 3-4:
# - tidak menerima input string
# - tidak negatif
# - tidak desimal


# latihan SET
# A = Himpunan Bilangan Genap dari 1-20
# B = Himpunan bilangan ganjil dari 1-20
# C = Himpunan bilangan negatif lebih besar -20
# D = Himpunan bilangan prima dari 1-20
# E = Himpunan bilangan komposit dari 1-20

# bilangan komposit = bukan bilangan prima

# U = Union
# n = Irisan

# a. A u B u C u D u E
# b. (A n B) u (D n E)
# c. (A u B) n (D u E)
# d. (A u B) - (D u E)
# e. (A u B u C) - (A n E)

# A = set()
# B = set()
# for i in range(21):
#     if i % 2 == 0:
#         A.add(i)
#     else:
#         B.add(i)
# print(f"A = {A}")
# print(f"B = {B}")
# C = set()
# for i in range(-20, 0):
#     C.add(i)
# print(f"C = {C}")

# D = set()
# E = set()
# for i in range(20):
#     if i > 1:
#         # print('loop i', i)
#         for j in range(2, i):
#             # print('loop j', j)
#             if (i % j) == 0:
#                 E.add(i)
#                 break
#             else:
#                 D.add(i)
#     else:
#         continue
# print(f"D = {D}")
# print(f"E = {E}")

# print("*"*50)
# # a. A u B u C u D u E
# print("soal a: ", A | B | C | D | E)
# # b. (A n B) u (D n E)
# print("soal b: ", (A & B) | (D & E))
# # c. (A u B) n (D u E)
# print("soal c: ", (A | B) & (D | E))
# # d. (A u B) - (D u E)
# print("soal d: ", (A | B) - (D | E))
# # e. (A u B u C) - (A n E)
# print("soal e: ", (A | B | C) - (A & E))


# string = ""

# x = int(input("Masukkan angka :"))
# bar = x
# # Looping Baris
# while bar >= 0:
#     # Looping Kolom Spasi Kosong
#     kol = bar
#     while kol > 0:
#         string = string + " . "
#         kol = kol - 1
#     # Looping Kolom Bintang Sisi Kiri
#     # kiri = 1
#     # while kiri < (x - (bar-1)):
#     #     string = string + " * "
#     #     kiri = kiri + 1
#     # # Looping Kolom Bintang Sisi Kanan
#     # kanan = 1
#     # while kanan < kiri - 1:
#     #     string = string + " * "
#     #     kanan = kanan + 1

#     string = string + "\n\n"
#     bar = bar - 1
# print(string)

# string = ""
# x = int(input("Masukkan angka :"))

# counter = x
# for i in range(6):
#     # looping spasi kosong
#     string += " . "
#     print(string)


# print(string)


# Latihan
# Auto - Translator
# Hari = {"senin": "monday",
#         "selasa": "tuesday",
#         "rabu": "wednesday",
#         "kamis": "thursday",
#         "jumat": "friday",
#         "sabtu": "saturday"}

# Input: masukkan nama hari: ...

# Kondisi:
# - tidak case sensitif
# - Tidak menerima inputan bukan hari, integer, float, dll

# Keluar notif: nama hari yang anda masukkan salah

# Output:
# tergantung inputan
# - jika inputan hari dalam bahasa Indonesia == > (f"Hari {hari} dalam bahasa Inggris adalah {eng}")
# - jika inputan hari dalam bahasa English == > (f"{hari} in bahasa Indonesia is {...}")

# latihan 20201126:
# email verification
# - buat sebuah return function dengan 1 argumen untuk mengecek/memvalidasi email

# input: masukkan email:

# kondisi:
# email valid jika:
# - memiliki format nama user@nama hosting.ekstensi
# - (check) nama user hanya boleh huruf, angka, underscore(_) dan dot (.)
# - (check) nama hosting hanya boleh huruf dan angka
# - (check) nama ekstensi hanya boleh huruf dan maksimal 5 karakter

# output:
# alamat email yang anda masukkan valid!!
# jika tidak valid, keluar alasannya:
# format email salah (misal tidak ada @ atau tidak ada .ekstensi)
# format username yang anda masukkan salah
# format hosting yang anda masukkan salah
# format ekstensi yang anda masukkan salah

# contoh email
# valid: andre@gmail.com, joni_12@yahoo.com, andy34@city.id, steve.roger_77@avengers01.space
# invalid: andre254@gmail.com, andre%^&@gmail.com, john_capt@yah^^oo.com, tony_stark@stark.corporation, Thor@@gmail.com


elif instruction == "update":
    exit_command = ""
    while exit_command != "1":
        print('\t\tUPDATE MENU')
        input_item = str(
            input("\t\t---> Enter item name to update: "))
        if input_item in car_list:
            update_item = str(
                input("\t\t---> Data has been registered.\n \t\tEnter the update?: "))
            for i in car_list:
                if i == input_item:
                    index = car_list.index(input_item)
                    car_list[index] = update_item
            print("\t\t'data has been updated'")
            for n, i in enumerate(car_list):
                print(f"\t\t{n+1}. {i}")
            # else:
            #     print("'data format is incorrect'")
        else:
            print("\t\t'the item is not in the list'")
            print("\t\t'please check your item in this list'")
            for n, i in enumerate(car_list):
                print(f"\t\t{n+1}. {i}")

        exit_command = str(
            input(f"1. back to main menu: (1) \n2. repeat menu {instruction}: (2) \n--->"))

    print("-"*70)

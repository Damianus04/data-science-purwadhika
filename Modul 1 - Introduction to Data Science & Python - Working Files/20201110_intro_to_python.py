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


# 20201112
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

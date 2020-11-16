# TASK 1
# Input: jumlah hari:
# output: ... tahun ... bulan .. minggu .. hari

# notes:
# 1 tahun = 365 hari
# 1 bulan = 30 hari

days = int(input("please input number of days: "))
n_year = 365
n_month = 30
n_week = 7

year = days // n_year  # 35 hari
days_mod = days % n_year
# print(days_mod)

month = days_mod // n_month
days_mod = days_mod % n_month
# print(days_mod)

week = days_mod // n_week
week_mod = days_mod % n_week
# print(days_mod)

day = int(week_mod)

print(year, "year,", month, "month,", week, "week", day, "day.")

# Alternative with "0"
days = int(input("please input number of days: "))
n_year = 365
n_month = 30
n_week = 7

year = days // n_year  # 35 hari
days_mod = days % n_year
# print(days_mod)

month = days_mod // n_month
days_mod = days_mod % n_month
# print(days_mod)

week = days_mod // n_week
week_mod = days_mod % n_week
# print(days_mod)

day = int(week_mod)


time = []
if year < 10:
    year_0 = "0" + str(year)
    time.append(year_0)
else:
    time.append(year)

if month < 10:
    day_0 = "0" + str(month)
    time.append(day_0)
else:
    time.append(day)

if week < 10:
    week_0 = "0" + str(week)
    time.append(week_0)
else:
    time.append(week)

if day < 10:
    day_0 = "0" + str(day)
    time.append(day_0)
else:
    time.append(day)

print(time[0], "year,", time[1], "month,", time[2], "week", time[3], "day.")

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
#             f"Your height is {height_m} m, your body mass is {mass} kg, your BMI is {BMI}, and you are {BMI_status}")
#     elif mass > 200:
#         print("body mass should be under 200 kg")
#     elif height > 300:
#         print("body height should be under 300 cm or 3 meter")
#     else:
#         print("mass and height cannot be lower than 1")

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
#             grade = "Grade B"
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

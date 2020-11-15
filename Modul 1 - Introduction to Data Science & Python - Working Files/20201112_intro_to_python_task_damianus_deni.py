# TASK 1
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


# TASK 2
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

# TASK 3
# Jumlah usia budi dan ayahnya sekarang adalah 50 tahun.
# 4 tahun lalu, usia ayah budi 6 kali usia budi.
# berapa usia ayah dan usia budi saat ini?

# Output:
# Usia ayah saat ini adalah ... tahun dan usia budi saat ini adalah ... tahun

total_usia = int(input("total_usia: "))
rasio_dulu = int(input("rasio dulu: "))
periode_lalu = int(input("masukkan periode ke belakang: "))
rasio_sekarang = int(input("masukkan rasio sekarang: "))

# usia_budi = int((total_usia + (rasio_usia * periode_lalu)) / 7)
# usia_ayah = int(total_usia - usia_budi)
usia_ayah = int((rasio_dulu * (total_usia - periode_lalu) +
                 periode_lalu)/(rasio_sekarang + rasio_dulu))
usia_budi = int(total_usia - usia_ayah)


print(
    f"Usia ayah saat ini adalah {usia_ayah} tahun dan usia budi saat ini adalah {usia_budi} tahun")

# kirim email: khumaeni@purwadhika.com

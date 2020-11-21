# ===Operator Perbandingan

# Output = TRUE dan FALSE  == Boolean

# a == b : Sama dengan
# a != b: Tidak sama dengan 
### Penggunaan Operator == dan != tidak mengharuskan menggunakan tipe data Numerik (Integer & Float)

#### Operator Perbadingan dibawah harus menggunakan Tipe data Numerik (Integer & Float)
# a < b : Kurang dari
# a > b : Lebih dari
# a <= b : Kurang dari atau sama dengan 
# a >= b : Lebih dari atau sama dengan 

# a = 5.5
# b = 7

# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)

# #### Operator Logika
# - Menghasilkan TRUE atau FALSE
# AND 
# OR 
# NOT ==> negasi ==> akan menghasilkan Kebalikan Not TRUE => FALSE, Not False => True 

# a AND b ==> akan menghasilkan TRUE JIKA a dan b TRUE, selain ini akan menghasilkan FALSE

# (a != b) AND (a < b)

if a and b and c and d or e :


# a OR b ==> Akan menghasilkan FALSE jika a dan b FALSE, selain ini akan menghasilkan TRUE

# (a == b) OR (a > b)

# ### Operator Gabungan
# ## Variabel harus sudah di definiskan terlebih dahulu
# angka = 30

# angka = angka + 5

# angka += 5

# angka = angka - 4

# angka -= 4

# angka = angka * 2

# angka *= 2

# angka = angka / 10

# angka /= 10

# pow(2, 3) ==> 2 pangkat 3
# 2 ** 3 ==> 2 pangkat 3

# angka = angka ** 2

# angka **= 2


# angka = angka % 7

# angka %= 7

angka = 15

angka *= 20

# print(angka)

### Operator Membership
## Menghasilkan TRUE atau FALSE
# in 
# not in 

nama = "Nama saya joni andre dan tinggal di jakarta"

# print("saya" in nama)
# print("bandung" in nama)

# print("saya" not in nama)
# print("bandung" not in nama)

# print(nama.replace("joni", "mike"))
# print(nama.split(" "))
# print(nama.split(" ", 1))
# print(nama.split("dan"))
# print(nama.count('j'))
# print(nama.count('r'))



# nilai = 8978512

# print(8 in nilai)

# Lat
# Input : Masukkan Jumlah Hari : 
# Output nya :
# Nyatakan jumlah hari tersebut dalam 
# ..Tahun ... Bulan ... minggu ... hari

# notes : 
# 1 tahun = 365 hari 
# 1 bulan = 30 hari

# contoh :
# Masukkan jumlah hari : 35

# 0 Tahun 1 Bulan 0 minggu 5 hari

# Input :
# Masukkan Kalimat :
# Masukkan Karakter : x
# Output :
# Jumlah Karakter x di dalam kalimat xxxxx adalah 5 

# Hari ini, HARI TidAK Masuk KulIAH
# masukkan karakter : a 
# 5

# IF Statement
# Pengecekan Kondisi

# Basic Syntax
if ....(Kondisi)...: ### Kondisi Harus BERNILAI TRUE agar Program dijalankan
    ...program..... ## Jika ada 1 Ketentuan

# if ...(Kondisi)... : (Jika ada 2 Ketentuan Gunakan if...else...)
#     Program u/ Ketentuan Pertama ===> Program ini akan dijalankan jika, Kondisi bernilai TRUE
# else:
#     program u/ ketentuan Kedua ===> Program ini akan dijalankan Jika, Kondisi Bernilai FALSE

# angka = 5

# if angka == 7:
#     print("Angka Sama")

# nilai = 90

# if nilai > 85:
#     print("Anda Lulus")
# else:
#     print("Anda Gagal")

# Jika ada beberapa ketentuan (Ketentuan lebih dari 2)
# if ...kondisi 1...:
#     program 1... ==> Program akan dijalankan jika Kondisi 1 bernilai TRUE 
# elif ...kondisi 2...:
#     program 2... ==> Program akan dijalankan jika Kondisi 2 bernilai TRUE 
# elif ...kondisi 3...:
#     program 3 ... ==> Program akan dijalankan jika kondisi 3 bernilai TRUE 
# else:
#     program 4  ==> Program 4 akan dijalankan JIKA, TIDAK ADA KONDISI yang bernilai TRUE 


### Nested IF
# ada IF di dalam IF 

# nilai = 90
# gender : "male"
kota = "jakarta"
if nilai > 85:
    if gender == "male":
        if kota == "jakarta":
            print("Mahasiswa Teladan Jakarta")
        elif kota =="surabaya":
            print("Mahasiswa Teladan Surabaya")
        elif kota =="bekasi":
            print("Mahasiswa Teladan Bekasi")
        else:
            print("Mahasiswa Teladan Bandung")
    else:
        print("Mahasiswi Teladan")


#### Error Handling
nilai = "Senin"

try:
    if nilai > 75:
        print("Anda Lulus")
    else:
        print("Anda gagal")
except:
    print("Nilai yang anda masukkan Salah")


# try:
#     Kondisi yg akan dilakukan pengecekan 
# except:
#     Program yg akan di run Jika ada Error di Kondisi


Lat
1.
Input : Masukkan Jumlah Hari : 
Output nya :
Nyatakan jumlah hari tersebut dalam 
..Tahun ... Bulan ... minggu ... hari

notes : 
1 tahun = 365 hari 
1 bulan = 30 hari

contoh :
Masukkan jumlah hari : 35

03 Tahun 10 Bulan 00 minggu 05 hari

2.
Input :
Masukkan Kalimat :
Masukkan Karakter : x
Output :
Jumlah Karakter x di dalam kalimat xxxxx adalah 5 

Hari ini, HARI TidAK Masuk KulIAH
masukkan karakter : a 
5

3. 
Input :
Masukkan Text : Hari ini adalah Hari Rabu
Masukkan Huruf Vokal : O i

Output :
Horo ono odoloh horo robo

hiri ini idilih hiri ribi

4. 
Hitung BMI (Body Mass Index)
Rumus BMI : massa (kg) / tinggi (dalam m) pangkat 2

Input :
Masukkan Tinggi Badan (dalam cm) :
Masukkan Massa (dalam kg) : 

Kondisi :
- Nilai Tinggi dan Massa tidak boleh Negatif ==> Keluar Notif "Tidak menerima Angka Negatif"
- Nilai Tinggi dan Massa tidak boleh String atau desimal ==> Notif "Angka yg anda masukkan salah"
- Batas Maksimal Massa : 200 kg dan tinggi 300cm ==> Notif "Tinggi / Massa yg anda masukkan diluar Batas"

Output :
Sesuaikan dg Hasil 
BMI < 18.5 ==> Berat Badan Kurang 
18.5 - 24.9 ==> Berat badan Ideal 
25 - 29.9 ==> Berat badan berlebih
30 - 39.9 ==> BB sangat berlebih 
BMI >= 40 ==> Obesitas

Tinggi badan anda .... m dan Massa anda ... kg, BMI anda .... (Nilai BMI) dan anda termasuk ....(sesuai kondisi)

5.
Input :
Masukkan Nilai : ...

Kondisi :
90 Keatas : Grade A 
85 Keatas : Grade A-
80 Keatas : Grade B
75 Keatas : Grade B-
70 Keatas : Grade C 
65 Keatas : Grade D
Dibawah 65 : Anda Tidak Lulus dan perlu Remedial

- Nilai Maksimum 100, nilai minimum 0 
- Jika nilai diatas 100 : Nilai diluar Jangkauan 
- Jika nilai dibawah 0 : Tidak menerima nilai Negatif 
- Jika Inputan Bukan angka : Angka yang anda masukkan Salah
- Bisa menerima Nilai Desimal 

Output :
Nilai Anda ..... Dan anda ....(Sesuai Kondisi)
Email 
khumaeni@purwadhika.com 
Deadline : Hari Senin jam 12 siang 
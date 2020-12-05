'''
Filter Function
- Comparison Function  (Function yg akan menghasilkan TRUE dan FALSE)
- Untuk Pengecekan Kondisi
Basic Syntax :
filter(Function, Data Iterable)

- Function hanya bisa 1
- Data Iterable juga hanya bisa 1
- Menghasilkan data Object, sehingga perlu dikonversi

Comparison - Conditional
>
<
>=
<=
OR, AND, dll 

TRUE dan FALSE
FILTER Hanya Akan Mengambil NILAI yg bernilai TRUE
'''

from functools import reduce
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hasil = list(filter(lambda x: x % 2 == 0, A))
print(hasil)

B = [26, 20, 10, 8, 70, 56, 89, 100, 5]


def cek(x): return 5 > x > 20


result = list(filter(cek, B))
print(result)

# ### REDUCE
# - Menghasilkan 1 value
# Basic Syntax :
# reduce(Function, Data Iterable)

# a = [1,2,3,4,5]
# x + y
# 1+2
# (1+2) + 3
# (1+2+3) + 4
# (1+2+3+4) + 5


F = [1, 2, 3, 4, 5, 6, 7, 8, 9]

hasil = reduce(lambda x, y: (x+y)*2, F)

print(type(hasil))

###
Berapa jumlah total bilangan ganjil yang telah dipangkatkan 3 dari rentang angka 1-200

Buat 1 baris perintah/fungsi(selain define Var)


### Tugas - Latihan

1.
Input: Masukkan Kalimat
"nama saya joni"
Output: "aman ayas inoj"

2.
Buat Algoritma
Buat List(Masukkan List inputan dari user)
-- Angka - Alfa
-- Numerik
Pilihan:
1. Ascending
2. Descending
3. Min - Max
Output sesuai pilihan
1. Angka akan di sort dari terkecil ke terbesar
2. Angka akan di sort dari terbesar ke terkcecil
3. Nilai Minimum dan Nilai Maximum

Tidak boleh menggunakan Fungsi Sort atau[::-1] atau min() atau max()
gunakan algoritma

3.
-Buat Algoritma Stats-
Buat List
- Cari Nilai
Modus: Nilai yg paling sering muncul
Median: Nilai tengah
Mean: Rata-rata
Q1 - Quartil 1 - 25%
Q3 - Quartil 3 - 75%
Outliers

4. Buat Return Function untuk Spin angka

Ada Deret Angka(List dalam list)
[[1 2 3 4 5],
 [6 7 8 9 10],
 [11 12 13 14 15],
 [16 17 18 19 20],
 [21 22 23 24 25]]

Input:
Masukkan Angka 1-3

Pilihan 1:
[[21, 16, 11, 6, 1],
 [22, 17, 12, 7, 2],
 [23, 18, 13, 8, 3],
 [24, 19, 14, 9, 4],
 [25, 20, 15, 10, 5]]

Pilihan 2:
[[25, 24, 23, 22, 21],
 [20, 19, 18, 17, 16],
 [15, 14, 13, 12, 11],
 [10, 9, 8, 7, 6],
 [5, 4, 3, 2, 1]]

Pilihan 3:
[[5, 10, 15, 20, 25],
 [4, 9, 14, 19, 24],
 [3, 8, 13, 18, 23],
 [2, 7, 12, 17, 22],
 [1, 6, 11, 16, 21]]

4.
Buat Return Function
Kalkulator: (+, -, /, *)
Inputan
input angka 1: 8
input angka 2: 10
masukkan operator: +

Output: Hasil Penjumlahan dari 8 + 10 = 18

5.
Buat Def Function
Fizz Buzz

Input: Masukkan Angka:
Output:
ANgka dari input user akan menjadi range dari 1 - inputan tersebut
Output nya
akan dicek seluruh angka tersebut
kemudian akan di print
angka yg habis dibagi 3 diubah menjadi Fizz
angka yg habis dibagi 5 diubah menjadi Buzz
angka yg habis dibagi 3 dan 5 menjadi FizzBuzz
angka lain akan dicetak normal

6.
Buat Def Function
Caesar Cipher
Masukkan kata: Joni
masukkan angka: 2
Output nya: lqpk
j + 2 = l
o + 2 = q
n + 2 = p
i + 2 = k

masukkan kata: Joni
masukkan angka: -2
Output: imlg

7.
Konversi Romawi
Buat Return Function
Gunakan Dict
Batasan Maksimal 4000
Keluar notif: Angka diluar jangkauan
Encoder - Decoder Angka Romawi

Silakan Masukkan Angka: 2018
Output nya: MMXVIII

Silakan Masukkan angka: MMXVIII
Output nya: 2018

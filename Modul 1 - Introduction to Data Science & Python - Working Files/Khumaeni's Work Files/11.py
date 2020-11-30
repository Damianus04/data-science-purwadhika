## def Function
'''
- Function yg akan dipake berkali-kali 
- Memiliki Nama 
- Fungsinya Generik - Umum

## Lambda Function
- Biasanya digunakan untuk Fungsi khusus  - Function yg sekali pake (Kecuali dimasukkan ke dalam def function atau Variabel)
- Anonymous Function - Function yg Tidak memiliki nama 
- memiliki ukuran kecil 
- Hanya memiliki satu program atau fungsi / Expresssion 
- Tidak ada Return Value 
- Lambda digunakan dg Meng-Assign fungsi nya ke dalam Variabel
- Atau Menggunakannya di dalam Def Function

## Basic Syntax

lambda Argumen : Expression 
- Jumlah Argumen Unlimited (Tidak terbatas)
- Expression => Progam / Fungsi hanya dapat 1 

Contoh :
# def pangkat(x):
#     hasil = x ** 2
#     return hasil 

# print(pangkat(5))

# def kali(x, y):
#     hasil = x * y
#     return hasil


lambda x : x ** 2  ## ==> 1 Argumen => x, Expression/fungsi/program => x ** 2
lambda kilo : kilo * 6000 ## 1 Argumen => Kilo, Expression/fungsi/program => kilo * 6000
lambda kilo, harga : kilo * harga ## 2 Argumen => Kilo, Harga. Expression/fungsi/program => kilo * harga
lambda x, y: x * y ## 2 argumen => x, y. Expression/fungsi/program => x * y
lambda kilo, harga, diskon : (kilo * harga) - diskon ## 3 argumen => kilo, harga, diskon. Expression/fungsi/prog => (kilo * harga) - diskon

'''

### Format Def Function
def penjumlahan(x, y):
    hasil = x + y
    return hasil

# def jumlah(x, y):
#     return x + y

def pangkat(x):
    hasil = x ** 2
    return hasil 

def triplet(a, b, c):
    hasil = a * b * c 
    return hasil

## Format Lambda Function 

# print(penjumlahan(5, 5))
# print(pangkat(5))
# print(triplet(5, 10, 20))
print('=' * 50)

### Menggunakan Lambda dengan Meng-Assign ke dalam Variabel
jumlah = lambda x, y: x + y
power = lambda x: x ** 2
triplet2 = lambda a, b, c : a * b * c 

# print(jumlah(5, 5))
# print(power(5))
# print(triplet2(5,10,20))

### Menggunakan Lambda dg Def Function (Memasukkan Lambda kedalam Def Funct.)
def myFunc(x):
    # hasil = lambda a : a ** x
    # return hasil
    return lambda a : a ** x ## x = 2, a = 10, 10 ** 2

# print(myFunc(2))  ### 2 adalah nilai x 

pangkat2 = myFunc(2) ### 2 => nilai x
pangkat3 = myFunc(3) ### 3 => nilai x

print(pangkat2(10)) ### 10 => nilai a
print(pangkat3(2)) ### 2 => nilai a

pangkat4 = myFunc(4) ### 4 => nilai x

print(pangkat4(5)) ### 5 => nilai a

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
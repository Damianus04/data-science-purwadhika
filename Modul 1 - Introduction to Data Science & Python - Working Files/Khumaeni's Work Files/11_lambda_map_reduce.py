# def Function
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
- Atau Menggunakannya di dalam Def Function atau Function Lain


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

# Format Def Function


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


# print(penjumlahan(5, 5))
# print(pangkat(5))
# print(triplet(5, 10, 20))
print('=' * 50)

# Format Lambda Function
# Menggunakan Lambda dengan Meng-Assign ke dalam Variabel


def jumlah(x, y): return x + y


def power(x): return x ** 2


def triplet2(a, b, c): return a * b * c

# print(jumlah(5, 5))
# print(power(5))
# print(triplet2(5,10,20))

# Menggunakan Lambda dg Def Function (Memasukkan Lambda kedalam Def Funct.)


def myFunc(x):
    # hasil = lambda a : a ** x
    # return hasil
    return lambda a: a ** x  # x = 2, a = 10, 10 ** 2


# print(myFunc(2))  ### 2 adalah nilai x
'''
pangkat2 = myFunc(2) ### 2 => nilai x
pangkat3 = myFunc(3) ### 3 => nilai x

# print(pangkat2(10)) ### 10 => nilai a
# print(pangkat3(2)) ### 2 => nilai a

pangkat4 = myFunc(4) ### 4 => nilai x
'''
# print(pangkat4(5)) ### 5 => nilai a

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


def myFunction(y):
    return lambda x: x * y


kali5 = myFunction(5)  # nilai y = 5

# print(kali5(10)) ### nilai x = 10

kali4 = myFunction(4)
'''
# print(kali4(10))
angka = 8
## Fungsi Konvensional
if angka%2 == 0:
    print("Genap")
else:
    print("Ganjil")
'''

# Def Function


def GanGen(x):
    if x % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

# print(GanGen(20))
# print(GanGen(257))
# print(GanGen(6982))


# Lambda Function
def CekGG(x): return True if x % 2 == 0 else False
# print(CekGG(57))

# print(CekGG(77))


def cekGG2(x): return "Angka Genap" if x % 2 == 0 else "Angka Ganjil"

# print(cekGG2(987))
# print(cekGG2(1234))

# Map Function
# Function yg Mirip dg Lambda Function
# Tapi digunakan untuk Data Iterables - Data Structures (List, Tuple, Dict, set, dll)


# Dengan 1 Argumen
A = [2, 70, 15, 81]


def kuadrat(x):
    hasil = x ** 2
    return hasil


def kuadrat2(x): return x ** 2

# print(kuadrat(5))
# print(kuadrat2(6))


# print(kuadrat(A))
# print(kuadrat2(A))
'''
Basic Syntax :
map(Function, Argumen)

Function = Fungsi yg akan digunakan untuk Argumen 
Argumen = Local Variabel yg akan digunakan sesuai dg Argumen pada Function 
Argumen = Berbentuk Data Iterable - Data Structures 
Jumlah Argumen Sesuai dengan Jumlah Argumen pada Function yg digunakan 
Hasil Operasional map, berupa Objek sehingga perlu dikonversi
'''
hasil = list(map(kuadrat, A))  # map menggunakan Def Funct
hasil2 = tuple(map(kuadrat, A))  # map menggunakan def function

# print(hasil)
# print(hasil2)
# x = 2
# hasil3 = list(map(x ** 2, A))

# print(hasil3)
'''
A = [2, 70, 15, 81]
hasil = []
for i in A:
    hasil.append(i ** 2)
'''

hasil3 = list(map(kuadrat2, A))  # map dengan Lambda Function
hasil4 = tuple(map(kuadrat2, A))  # map dengan lambda function
# print(hasil3)
# print(hasil4)

map(kuadrat2, A)

hasil5 = list(map(lambda x: x**2, A))
A = [2, 70, 15, 81]
B = []
for i in range(len(A)):
    if i == 0 or i == 2:
        B.append(A[i])
hasil6 = list(map(kuadrat2, A[2:]))
# print(hasil6)


# Dengan 2 Argumen

# def function
def pangkat6(x, y):
    hasil = x ** y
    return hasil

# Lambda function


def jumlah2(x, y): return x + y


A = [1, 2, 3]
B = [10, 20, 30, 40, 50]

hasil = list(map(jumlah2, A, B))

# print(hasil)

hasil2 = list(map(lambda x, y: x + y, A, B))
# print()
# print(hasil2)


# dengan 3 argumen
A = [2, 5, 6]
B = [10, 20, 30]
C = [9, 8, 7]

# Def function


def triple(x, y, z):
    hasil = x * y * z
    return hasil


hasil = list(map(triple, A, B, C))
# print(hasil)


# lambda function
def triple2(x, y, z): return x * y * z


hasil = list(map(triple2, A, B, C))
# print(hasil)


hasil = list(map(lambda x, y, z: x * y * z, A, B, C))
# print(hasil)

D = [10, 15, 20, 30]

### D * (D ** 2)


def power1(x):
    hasil = x ** 2
    return hasil


def kali(x, y):
    hasil = x * y
    return hasil


def calc(x):
    y = x ** 2
    return x * y


E = list(map(power1, D))

hasil = list(map(kali, D, E))

# print(hasil)


def pangkat2(x): return x ** 2


def perkalian(x, y): return x * y


def calc2(x): return x * (x**2)


F = list(map(pangkat2, D))
hasil = list(map(perkalian, D, F))
# print(hasil)


F2 = list(map(lambda x: x ** 2, D))

hasil = list(map(perkalian, D, F2))
# print(hasil)

hasil = list(map(perkalian, D, list(map(lambda x: x ** 2, D))))

# print(hasil)


hasil = list(map(lambda x, y: x * y, D, list(map(lambda x: x ** 2, D))))
# print(hasil)

###################################


A = [1, 2, 3, 4, 5]

### (A ** 2) + ((A ** 2) * 3) + ((A ** 2) * 5)
'''
def kalkulasi(angka):
    hasil = []
    for i in angka:
        x = i ** 2
        D = x + (x * 3) + (x * 5)
        hasil.append(D)
    return hasil

print(kalkulasi(A))

calcL = lambda i: (i ** 2) + ((i**2)*3) + ((i**2)*5)

hasil = list(map(calcL, A))
print(hasil)
'''
A = [1, 2, 3, 4, 5]

### (A ** 2) + ((A ** 2) * 3) + ((A ** 2) * 5)


def pangkat2(i): return i ** 2


def kali3(x): return x * 3


def kali5(x): return x * 5


def jumlahkan(j, k, l): return j + k + l

# print(pangkat2(10))
# print(kali3(5))
# print(kali5(7))
# print(jumlahkan(5,10,15))

# print(A)


E = list(map(pangkat2, A))  # ==> (A ** 2)

# print(E)

F = list(map(kali3, E))  # ==> (A ** 2) * 3

# print(F)

G = list(map(kali5, E))  # (A ** 2) * 5
# print(G)

# (A ** 2) + ((A ** 2) * 3) + ((A ** 2) * 5)
result = list(map(jumlahkan, E, F, G))
print(result)

E1 = list(map(lambda i: i ** 2, A))  # ==> (A ** 2)
# print(E1)

F1 = list(map(kali3, list(map(lambda i: i ** 2, A))))  # ==> (A ** 2) * 3
# print(F1)

G1 = list(map(kali5, list(map(lambda i: i ** 2, A))))  # (A ** 2) * 5
# print(G1)

result2 = list(map(jumlahkan, list(map(lambda i: i ** 2, A)), F, G))

print(result2)


F2 = list(map(lambda x: x * 3, list(map(lambda i: i ** 2, A))))
# print(F2)

G2 = list(map(lambda x: x * 5, list(map(lambda i: i ** 2, A))))

# print(G2)

# F = F1 = F2
result3 = list(map(jumlahkan, list(map(lambda i: i ** 2, A)),
                   list(map(lambda x: x * 3, list(map(lambda i: i ** 2, A)))), G))
print(result3)

# G = G1 = G2
result4 = list(map(jumlahkan, list(map(lambda i: i ** 2, A)),  # E
                   list(map(lambda x: x * 3, list(map(lambda i: i ** 2, A)))),  # F
                   list(map(lambda x: x * 5, list(map(lambda i: i ** 2, A))))))  # G

print(result4)

result5 = list(map(lambda j, k, l: j + k + l, list(map(lambda i: i ** 2, A)),  # E
                   list(map(lambda x: x * 3, list(map(lambda i: i ** 2, A)))),  # F
                   list(map(lambda x: x * 5, list(map(lambda i: i ** 2, A))))))  # G

print(result5)

# calcL = lambda i: (i ** 2) + ((i**2)*3) + ((i**2)*5)

# hasil = list(map(calcL, A))
# print(hasil)

###################################################


def Func1(i): return i ** 2


R = list(map(Func1, A))

result6 = list(map(lambda j, k, l: j + k + l, list(map(lambda i: i ** 2, A)),  # E
                   list(map(lambda x: x * 3, list(map(lambda i: i ** 2, A)))),  # F
                   list(map(lambda x: x * 5, R))))

print(result6)

result7 = list(map(lambda j, k, l: j + k + l, R,  # E
                   list(map(lambda x: x * 3, R)),  # F
                   list(map(lambda x: x * 5, R))))

print(result7)


def Func2(x): return x * 5


S = list(map(Func2, R))

result7 = list(map(lambda j, k, l: j + k + l, R,  # E
                   list(map(lambda x: x * 3, R)),  # F
                   S))
print(result7)


def Func3(x): return x * 3


T = list(map(Func3, R))
result8 = list(map(lambda j, k, l: j + k + l, R,
                   T,
                   S))
print(result8)


def jumlah2(j, k, l): return j + k + l


result9 = list(map(jumlah2, R, T, S))
print(result9)

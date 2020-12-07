# ⭐Soal 1 - Fungsi Pangkat
# Buatlah sebuah return function dengan 2 parameter yang dapat menghitung pangkat tertentu dari
# sebuah bilangan, tanpa menggunakan operator pangkat(**), tanpa menggunakan fungsi pow() dan
# tanpa memanfaatkan package/library manapun!


# ⭐Soal 2 - Kategori Bilangan
# Buatlah sebuah file Python yang mengandung sebuah return function untuk menentukan kategori
# bilangan sebuah angka. Misal: angka 13 tergolong bilangan bulat, cacah, asli, ganjil & prima.
# Berikut adalah definisi & pengkategorian bilangan menurut laman Wikipedia (klik di sini):

# Bilangan Bulat: Bilangan yang terdiri atas bilangan cacah (0, 1, 2, 3, ...) beserta nilai
# negatifnya (0, -1, -2, -3, ...). Bilangan bulat dapat dituliskan tanpa komponen desimal atau
# pecahan.

# Bilangan Cacah: Himpunan bilangan bulat yang tidak bernilai negatif, yaitu (0, 1, 2, 3 ...).

# Bilangan Negatif: Himpunan bilangan bulat yang nilainya lebih kecil dari 0, yaitu (-1, -2, -3, ...)

# Bilangan Nol: Yaitu 0

# Bilangan Asli: Himpunan bilangan cacah positif yang bukan nol, yaitu (1, 2, 3, ...)

# Bilangan Ganjil: Himpunan bilangan asli positif yang nilainya tidak habis dibagi 2,
# yaitu (1, 3, 5, 7, 9, ...)

# Bilangan Genap: Himpunan bilangan asli positif yang nilainya habis dibagi 2,
# yaitu (2, 4, 6, 8, 10, ...). Bilangan nol (0) juga digolongkan sebagai bilangan genap.

# Bilangan Prima: Himpunan bilangan asli yang nilainya lebih besar daripada 1,
# yang faktor pembaginya adalah 1 dan bilangan itu sendiri. 2 dan 3 adalah bilangan prima.
# 4 bukan bilangan prima karena dapat dibagi 2.

# Bilangan Komposit: Himpunan bilangan asli yang nilainya lebih besar daripada 1,
# yang bukan merupakan bilangan prima.

# ⭐Soal 3 - FPB & KPK
# Buatlah sebuah file Python interaktif yang mengandung sebuah function untuk menentukan
# nilai FPB (Faktor Persekutuan Besar) & KPK (Kelipatan Persekutuan Kecil) dari 2 buah bilangan.
# Pembahasan seputar FPB & KPK pernah kita pelajari bersama di bangku Sekolah Dasar,
# masih ingat dong?
# source: https://github.com/anastasyaviviana/Latihan_Ujian_FPB_KPK

'''
def fpb(a, b):
    fpb = ""
    if a < b:
        smaller = a
    else:
        smaller = b
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            fpb = i
        # else:
        #     continue

    return fpb

def kpk(a, b):
    kpk = int(a*b/fpb(a, b))
    return kpk


a = int(input('Masukkan angka pertama :'))
b = int(input('Masukkan angka kedua   :'))

print('FPB dari ', a, ' dan ', b, ' adalah ', fpb(a, b))
print('KPK dari ', a, ' dan ', b, ' adalah ', kpk(a, b))
'''

# ⭐Soal 4 - ascending and descending list
# Buatlah sebuah return function dengan 1 parameter yang dapat membalik urutan elemen dari
# suatu list. Misal terdapat suatu list: [1,2,3,4,5] maka function yang Anda buat dapat
# membalik urutan elemen list menjadi: [5,4,3,2,1].
# Namun Anda dilarang keras untuk menggunakan cara-cara berikut:
# Cara 1. menggunakan reverse( ) method pada list
# a = [1, 2, 3, 4]
# a.reverse()
# print(a)

# // hasil = [4, 3, 2, 1]

# Cara 2. menggunakan list slicing syntax ( [ : : -1] )
# b = [5, 6, 7, 8]
# print(b[::-1])

# // hasil = [8, 7, 6, 5]

# Cara 3: menggunakan reversed( ) function
# c = [9, 10, 11, 12]
# print(list(reversed(c)))

# // hasil = [12, 11, 10, 9]

'''
def input_list():
    input_list = []
    list_length = int(input("length of list: "))
    for i in range(0, list_length):
        index = int(input(f"index {i+1}: "))
        input_list.append(index)
    return input_list


def min_sort(input_list):
    temporary_order = input_list[0]

    for i in range(len(input_list)):
        if temporary_order < input_list[i]:
            temporary_order = temporary_order
        else:
            temporary_order = input_list[i]

    return temporary_order


def max_sort(input_list):
    temporary_order = input_list[0]

    for i in range(len(input_list)):
        if temporary_order > input_list[i]:
            temporary_order = temporary_order
        else:
            temporary_order = input_list[i]

    return temporary_order


def ascending_list(input_list):
    input_list_copy = input_list[:]
    ascending_list = []
    asc_order = ""
    for i in range(len(input_list_copy)):
        if len(input_list_copy) != 0:
            asc_order = min_sort(input_list_copy)
            reduced_list = input_list_copy.remove(asc_order)
        ascending_list.append(asc_order)
    return ascending_list


def descending_list(input_list):
    input_list_copy = input_list[:]
    descending_list = []
    desc_order = ""
    for i in range(len(input_list_copy)):
        if len(input_list_copy) != 0:
            desc_order = max_sort(input_list_copy)
            reduced_list = input_list_copy.remove(desc_order)
        descending_list.append(desc_order)
    return descending_list


# execution
try:
    input_list = input_list()
    sort_mode = input("""sort mode:
        - Ascending (1)
        - Descending (2)
        - Min-Max (3)
    --> """)

    if sort_mode == "1":
        result = ascending_list(input_list)
        print(f"ascending_list: {result}")
    elif sort_mode == "2":
        result = descending_list(input_list)
        print(f"descending list: {result}")
    elif sort_mode == "3":
        min_number = min_sort(input_list)
        max_number = max_sort(input_list)
        print(f"min number is '{min_number}' and max number is '{max_number}'")
    else:
        print("you don't enter the correct option")

except:
    print("input should be integer")
'''

# ⭐Soal 5: Himpunan
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
'''
A = set()
B = set()
for i in range(1, 21):
    if i % 2 == 0:
        A.add(i)
    else:
        B.add(i)
print(f"Bilangan Genap A = {A}")
print(f"Bilangan Ganjil B = {B}")
C = set()
for i in range(-20, 0):
    C.add(i)
print(f"Bilangan Negatif C = {C}")

D = set()
E = set()

for i in range(20):
    if i == 2:
        D.add(i)
    elif i > 1:
        # print('loop i main', i)
        for j in range(2, i):
            # print('loop j', j)
            # print('loop i', i)
            if (i % j) == 0 or i == 2:
                E.add(i)
                break
            else:
                D.add(i)
    else:
        continue
print(f"Bilangan Prima D = {D}")
print(f"Bilangan Komposit E = {E}")
'''
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


# ⭐Soal 6 - 🔺 Segitiga Kata
# Buatlah sebuah file python (.py) yang mengandung sebuah function dengan 1 parameter,
# yang dapat membentuk pola segitiga dengan elemen berupa karakter-karakter dari sebuah
# string yang menjadi parameter function tersebut. Info selengkapnya silakan ikuti case flow
# beserta output yang diharapkan berikut ini.

# Case Flow: Saat dieksekusi, program akan mencetak pola segitiga dari karakter-karakter
# string yang diinputkan. Jika jumlah karakter string memenuhi syarat terbentuknya pola,
# maka program akan menjalankannya. Namun jika jumlah karakter string tidak memenuhi syarat
# membentuk pola, maka akan muncul pesan bahwa string tidak memenuhi syarat membentuk pola.

# segitigaKata('Purwadhika')
# segitigaKata('Purwadhika Startup and Coding School @BSD')
# segitigaKata('kode')
# segitigaKata('kode python')
# segitigaKata('lintang')
# Output yang diharapkan:

# # segitigaKata('Purwadhika')
# P
# u r
# w a d
# h i k a
# p u r w
# a d h
# i k
# a

# # segitigaKata('Purwadhika Startup and Coding School @BSD')
# P
# u r
# w a d
# h i k a
# S t a r t
# u p a n d C
# o d i n g S c
# h o o l @ B S D
# P u r w a d h i
# k a S t a r t
# u p a n d C
# o d i n g
# S c h o
# o l @
# B S
# D

# # segitigaKata('kode')
# Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.

# # segitigaKata('kode python')
# k
# o d
# e p y
# t h o n
# k o d e
# p y t
# h o
# n

# # segitigaKata('lintang')
# Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.

# text = "Purwadhika"
# multiplier = 0
# star = ""
# for i in range(len(text)//2):
#     for j in range(len(text)):
#         star += text[i]

#     multiplier += 1
#     print(star)


# multiplier = len(text)//2 - 1
# star = ""
# for i in range(len(text)//2):
#     star = " * " * (multiplier)
#     multiplier -= 1
#     print(star)

# solution from https://stackoverflow.com/questions/42606054/right-triangle-shaped-words-and-numbers-in-python-3
word = 'Purwadhika'


# word = word_input.replace(" ", "")
# print(word_split)

def triangle_1(word):
    line = 0
    start = 0
    end = 0
    suffix = ''
    done = False

    while not done:
        start = end

        end = start + line + 1

        # Kondisi untuk membuat looping berhenti
        if end > len(word):
            done = True

        # print(word[start:end] + "")

        letters = word[start:end].split(" ")
        letters_list = []
        for i in letters:
            letters_list.append(i)

        x = ""
        for i in letters_list:
            x += i

        print(x)

        line += 1


def triangle_2(message, size):
    # Size = 0: we're done; ran out of rows
    if size == 0:
        return
    # Not enough message left: print it all
    if size >= len(message):
        print(message)
    # print "size" characters and go to next line
    else:
        print(message[:size])
        triangle_2(message[size:], size-1)


text = "kode python"


def word_triangle(text):
    triangle_1(text)
    triangle_2(text, 0)
    triangle_2(text, 4)


print(word_triangle(text))


# if start+1 < len(word):
#     while word[start] == '':
#         start += 1
#         print(start)


# ⭐Soal 7 - 🆒 Mengurai & Merajut Kata
# Buatlah sebuah file python (.py) yang berisi sebuah class dengan 2 buah method, yaitu urai(string) dan rajut(string). Dengan class tersebut, buatlah sebuah object yang dapat digunakan untuk mengurai & merajut sebuah string.

# # buat sebuah class dengan 2 method
# class uraiRajutKata:
#     def urai(...):
#         ...
#     def rajut(...):
#         ...

# # buat sebuah object
# x = uraiRajutKata()
# Method urai(string) akan mengurai string. Adapun cara pemanggilan method urai(string) dan contoh output yang diharapkan adalah sebagai berikut:

# print(x.urai('Code'))
# print(x.urai('Python'))
# print(x.urai('Purwadhika'))

# # Output:
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
# Sedangkan method rajut(string) akan merajut kembali string yang terurai menjadi bentuk kata asalnya. Adapun cara pemanggilan method rajut(string) dan contoh output yang diharapkan adalah sebagai berikut:

# print(x.rajut('CCoCodCode'))
# print(x.rajut('PPyPytPythPythoPython'))
# print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# # Output:
# Code
# Python
# Purwadhika

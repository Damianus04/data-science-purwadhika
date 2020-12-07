# Berapa jumlah total bilangan ganjil yang telah dipangkatkan 3 dari rentang angka 1-200

'''
# Buat 1 baris perintah/fungsi (selain define Var)
from functools import reduce

# steps
# number = []
# for i in range(1, 201):
#     number.append(i)
# 1) result = list(map(lambda i: i ** 3, number))
# 2) result_odd = list(filter(lambda i: i % 2 != 0, result))
# 3) result_odd = list(filter(lambda i: i %
#                          2 != 0, list(map(lambda i: i ** 3, number))))

result_odd_sum = reduce(lambda x, y: (x + y), list(filter(lambda i: i %
                                                          2 != 0, list(map(lambda i: i ** 3, list(range(201)))))))

print(result_odd_sum)

print("#"*50)

# 1.
# Input: Masukkan Kalimat
# "nama saya joni"
# Output: "aman ayas inoj"

try:
    text = input("type your text: ")
    #text_split = text.split(" ")
    #text_reverse = list(map(lambda x: x[::-1], text_split))
    #text_reverse_join = " ".join(text_reverse)

    text_reverse_join = " ".join(list(map(lambda x: x[::-1], text.split(" "))))
    # print(text_split)
    # print(text_reverse)
    print(text_reverse_join)
except:
    print("error")

print("#"*50)

# 2.
# Buat Algoritma
# Buat List(Masukkan List inputan dari user)
# -- Angka - Alfa
# -- Numerik
# Pilihan:
# 1. Ascending
# 2. Descending
# 3. Min - Max
# Output sesuai pilihan
# 1. Angka akan di sort dari terkecil ke terbesar
# 2. Angka akan di sort dari terbesar ke terkcecil
# 3. Nilai Minimum dan Nilai Maximum

# Tidak boleh menggunakan Fungsi Sort atau[::-1] atau min() atau max()
# gunakan algoritma

# functions

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

print("#"*50)

# 3.
# -Buat Algoritma Stats-
# Buat List
# - Cari Nilai
# Modus: Nilai yg paling sering muncul
# Median: Nilai tengah
# Mean: Rata-rata
# Q1 - Quartil 1 - 25%
# Q3 - Quartil 3 - 75%
# Outliers


# def input_list():
#     input_list = []
#     list_length = int(input("length of list: "))
#     for i in range(0, list_length):
#         index = int(input(f"index {i+1}: "))
#         input_list.append(index)
#     return input_list


# list_number = input_list()
# print(list_number)

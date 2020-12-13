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
'''
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


list_number = [56, 220, 4, 45, 6, 13, 10, 45, 6, 10, 100, 1]

# mean


def mean(list_number):
    sum = 0
    for i in range(len(list_number)):
        sum += list_number[i]
    mean = round(sum / len(list_number), 2)
    return mean


# med

def med(list_number):
    ascending_result = ascending_list(list_number)

    if len(ascending_result) % 2 == 0:
        half_index = len(ascending_result)//2
        half_index_minus_1 = half_index - 1
        median = (ascending_result[half_index] +
                  ascending_result[half_index_minus_1]) / 2
    else:
        half_index = len(ascending_result)//2
        median = ascending_result[half_index]

    return median

# mod


def mod(list_number):
    list_number_unique = list(set(list_number))

    result = {}

    for i, j in enumerate(list_number_unique):
        sum = list_number.count(j)
        output = {f"{j}": sum}
        result.update(output)

    result_values = list(result.values())
    result_keys = list(result.keys())

    mod_temp = max_sort(result_values)
    mod = result_keys[result_values.index(mod_temp)]

    return mod


input_number = [56, 220, 4, 45, 13, 10, 45, 6, 10, 100, 1]
# input_number = [1, 4, 6, 6, 10, 10, 13, 45, 45, 56, 100, 220]

print(med(input_number))
print(mean(input_number))
print(mod(input_number))
'''
print("#"*50)

# 4. Buat Return Function untuk Spin angka

# Ada Deret Angka(List dalam list)
# input_list = [[1, 2, 3, 4, 5],
#  [6, 7, 8, 9, 10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25]]

# Input:
# Masukkan Angka 1-3

# Pilihan 1:
# [[21, 16, 11, 6, 1],
#  [22, 17, 12, 7, 2],
#  [23, 18, 13, 8, 3],
#  [24, 19, 14, 9, 4],
#  [25, 20, 15, 10, 5]]

# Pilihan 2:
# [[25, 24, 23, 22, 21],
#  [20, 19, 18, 17, 16],
#  [15, 14, 13, 12, 11],
#  [10, 9, 8, 7, 6],
#  [5, 4, 3, 2, 1]]

# Pilihan 3:
# [[5, 10, 15, 20, 25],
#  [4, 9, 14, 19, 24],
#  [3, 8, 13, 18, 23],
#  [2, 7, 12, 17, 22],
#  [1, 6, 11, 16, 21]]


def option1(input_list):
    temp_list = []
    x = 0
    input_list = input_list[::-1]
    for i, j in enumerate(input_list):
        for k in range(len(input_list[x])):
            temp_list.append(input_list[k][x])
        x += 1

    main_list = []
    x = 0
    y = len(input_list[0])

    for i in range(len(input_list[0])):
        main_list.append(temp_list[x:y])
        x += len(input_list[0])
        y += len(input_list[0])

    main_list = main_list[::]
    return main_list


def option2(input_list):
    temp_list = []
    x = 0
    for i, j in enumerate(input_list):
        temp_list.append(j[::-1])
        x += 1
    main_list = temp_list[::-1]
    return main_list


def option3(input_list):
    temp_list = []
    x = 0
    for i, j in enumerate(input_list):
        for k in range(len(input_list[x])):
            temp_list.append(input_list[k][x])
        x += 1

    main_list = []
    x = 0
    y = len(input_list[0])

    for i in range(len(input_list[0])):
        main_list.append(temp_list[x:y])
        x += len(input_list[0])
        y += len(input_list[0])

    main_list = main_list[::-1]
    return main_list


input_list = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]

op1 = option1(input_list)
op2 = option2(input_list)
op3 = option3(input_list)

print(f"{op1}\n{op2}\n{op3}")


print("#"*50)

'''
# 5.
# Buat Return Function
# Kalkulator: (+, -, /, *)
# Inputan
# input angka 1: 8
# input angka 2: 10
# masukkan operator: +

# Output: Hasil Penjumlahan dari 8 + 10 = 18


def addition(x, y):
    result = x + y
    return result


def substration(x, y):
    result = x - y
    return result


def multiply(x, y):
    result = x * y
    return result


def division(x, y):
    result = x / y
    return result


def calculation(x, y, operator):
    if operator == "addition" or operator == "+":
        result = addition(x, y)
        return result
    elif operator == "substration" or operator == "-":
        result = substration(x, y)
        return result
    elif operator == "multiply" or operator == "*" or operator == "x":
        result = multiply(x, y)
        return result
    elif operator == "division" or operator == "/" or operator == ":":
        result = division(x, y)
        return result
    else:
        return "please select the operator"


def calculator():
    try:
        x = int(input("type number 1: "))
        y = int(input("type number 2: "))
        operator = input("select the operator: ")

        result = calculation(x, y, operator)
        output = f"the result of {x} {operator} {y} is {result}"

        return output
    except:
        return "calculation error, please select the correct number and operator"


print(calculator())
'''
print("#"*50)

# 6.
# Buat Def Function
# Fizz Buzz

# Input: Masukkan Angka:
# Output:
# ANgka dari input user akan menjadi range dari 1 - inputan tersebut
# Output nya
# akan dicek seluruh angka tersebut
# kemudian akan di print
# angka yg habis dibagi 3 diubah menjadi Fizz
# angka yg habis dibagi 5 diubah menjadi Buzz
# angka yg habis dibagi 3 dan 5 menjadi FizzBuzz
# angka lain akan dicetak normal

print("#"*50)

# 7.
# Buat Def Function
# Caesar Cipher
# Masukkan kata: Joni
# masukkan angka: 2
# Output nya: lqpk
# j + 2 = l
# o + 2 = q
# n + 2 = p
# i + 2 = k

# masukkan kata: Joni
# masukkan angka: -2
# Output: imlg

print("#"*50)


# 8.
# Konversi Romawi
# Buat Return Function
# Gunakan Dict
# Batasan Maksimal 4000
# Keluar notif: Angka diluar jangkauan
# Encoder - Decoder Angka Romawi

# Silakan Masukkan Angka: 2018
# Output nya: MMXVIII

# Silakan Masukkan angka: MMXVIII
# Output nya: 2018

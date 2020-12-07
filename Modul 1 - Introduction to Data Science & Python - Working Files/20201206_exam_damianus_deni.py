Soal 1 - Konversi Waktu(30 Poin)
Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu("HH:MM:SS").

HH: Hours, 2 digits, range: 00 - 99

MM: Minutes, 2 digits, range: 00 - 59

SS: Seconds, 2 digits, range: 00 - 59

Case Flow: Saat dieksekusi, program akan mencetak nilai return function.


def timeConverter(seconds):
    .....


Masukkan detik: 3600
Konversi: 01: 00: 00

Masukkan detik: 3665
Konversi: 01: 01: 05
Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, jika user memasukkan nilai lebih dari 359999, bilangan desimal, bilangan negatif, maupun memasukkan string akan keluar notifikasi. Invalid Input

Masukkan detik: ujian
Invalid Input!

Masukkan detik: 20.5
Invalid Input!


def timeConverter(input_second):
    try:
        input_second = int(input("type time in second: "))
        n_hour = 3600
        n_minute = 60

        if 0 <= input_second <= 359999:
            # Calculation Part
            hour = input_second // n_hour
            seconds_mod = input_second % n_hour

            minute = seconds_mod // n_minute
            seconds_mod = seconds_mod % n_minute

            second = seconds_mod

            # Display Part
            time = []

            if hour < 10:
                hour_0 = "0" + str(hour)
                time.append(hour_0)
            else:
                time.append(hour)

            if minute < 10:
                minute_0 = "0" + str(minute)
                time.append(minute_0)
            else:
                time.append(minute)

            if second < 10:
                second_0 = "0" + str(second)
                time.append(second_0)
            else:
                time.append(second)

            output = f"Convertion: {time[0]}:{time[1]}:{time[2]}"

            return output
        else:
            return 'Invalid Input!'
    except:
        return 'Invalid Input'


print(timeConverter(3600))

#
#
#
#
#
# NOTES
# time1 = 3600
# time2 = 3665
# time3 = 359999
# time4 = 498909
# time5 = -18900
# time6 = 0.98

# def print_time_converter(input):
#     output = timeConverter(input)
#     print(f"{input} \t --> {output}")


Soal 2 - List Spinner(30 Poin)
Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka(Putaran 1X counter-clockwise) seperti keterangan di bawah ini .

List Awal

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Function

# Function Initialization


def counterClockwise(...):
    .....


# Use the Function
print(counterClockwise(List_awal))
List Output

[[3, 6, 9],
 [2, 5, 8],
 [1, 4, 7]]


Soal 3 - Mengurai dan Merajut Kata(40 Poin)
Buatlah sebuah file python yang berisi 2 buah return function, dengan 1 argumen yang dapat digunakan untuk mengurai & merajut sebuah string

fungsi urai(...) akan mengurai string. contoh output yang diharapkan adalah sebagai berikut:

    # Function Initialization :


def urai(...):
    ......


def rajut(...):
    ......


# Use the function

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

# Output:
CCoCodCode
PPyPytPythPythoPython
PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
Sedangkan fungsi rajut(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya. contoh output yang diharapkan adalah sebagai berikut:

    # Use the function

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# Output:

Code
Python
Purwadhika


# 1) URAI Function
def urai(text):
    output = ""

    for i, j in enumerate(text):
        output = output + text[:i+1]

    return output


# print(urai('Code'))
# print(urai('Python'))
# print(urai('Purwadhika'))


# 2) RAJUT Function
def rajut(text):
    output = ""

    text_list = list(text)
    text_set = set(text_list)

    for i in text_list:
        if i in text_set:
            output += i
            text_set.remove(i)

    return output


print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

#
#
#
#
#
# NOTES
# for i, j in enumerate(text):
#     for k, l in enumerate(text):
#         if text[i] == text[k]:
#             output += text[i]
#         elif text[i] != text[k]:
#             # output += text[k]
#             continue

# for i, j in enumerate(text):
#     if i+1 < len(text):
#         if text[i] == text[i+1]:
#             continue
#         elif text[i] != text[i+1]:
#             output += text[i]


# for i, j in enumerate(text):
#     for k in range(len(text)):
#         output = output + text[:k]

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
'''
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

try:
    list = []
    list_length = int(input("type the length of the list: "))
    for i in range(0, list_length):
        element = int(input(f"element {i+1}: "))
        list.append(element)
    sort_mode = input("""sort mode:
        - Ascending (1)
        - Descending (2)
        - Min-Max (3)
    --> """)

    if sort_mode == "1":
        asc_list = []
        for i in list:
            while i < i+1:
                asc_list.append(i)
        print(f"ascending list: {asc_list}")
    elif sort_mode == "2":
        print(f"descending list: ")
    elif sort_mode == "3":
        minmax = []
        x = ""
        for i in range(len(list)):
            # print(i)
            if i+1 < len(list):
                if list[i] < list[i+1]:
                    x = list[i]
                else:
                    x = list[i+1]
            else:
                break
        minmax.append(x)

        print(f"min number is '{minmax}' and max number is ''")
    else:
        print("you don't enter the correct option")

except:
    print("input should be integer")

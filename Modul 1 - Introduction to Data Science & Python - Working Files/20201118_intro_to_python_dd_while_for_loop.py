'''
# Soal 1
print("soal 1")

try:
    bottom_limit = 0
    top_limit = int(input("type your number: "))

    while bottom_limit < top_limit:
        bottom_limit += 1
        bottom_limit_string = str(bottom_limit) + " "
        print(bottom_limit_string * bottom_limit)
except:
    print("error occurs, type only integer number")

print("-"*50)


# Soal 2
print("soal 2")

try:
    bottom_limit = 0
    top_limit = int(input("type your number: "))
    output = ""

    while bottom_limit < top_limit:
        bottom_limit += 1
        bottom_limit_string = str(bottom_limit) + " "
        output += bottom_limit_string

        print(output)
except:
    print("error occurs, type only integer number")

print("-"*50)

# Soal 3
print("soal 3")
try:
    top_limit = int(input("type your number: "))
    bottom_limit = 1
    output = ""

    while top_limit > bottom_limit:
        top_limit -= 1
        top_limit_string = str(top_limit) + " "
        output += top_limit_string

        print(output)
except:
    print("error occurs, type only integer number")

print("-"*50)

# Soal 4
print("soal 4")
try:
    top_limit = int(input("type your number: "))
    bottom_limit = 0
    counter = 0

    while top_limit > bottom_limit:
        top_limit -= 1
        counter += 1
        counter_string = str(counter) + " "
        print(counter_string * top_limit)
except:
    print("error occurs, type only integer number")

print("-"*50)

# Soal 5
print("soal 5")
try:
    top_limit = int(input("type your number: "))
    bottom_limit = 0
    output = ""

    while bottom_limit < top_limit:
        bottom_limit += 1
        bottom_limit_string = str(bottom_limit) + " "
        output += bottom_limit_string

    print(f"checker: {output}")

    counter = 0
    for i in range(len(output)):
        counter += 1
        if output[i] == " ":
            continue
        else:
            print(output[:-counter])

        i += 1
except:
    print("error occurs, type only integer number")

print("-"*50)


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Soal 6
print("soal 6")
try:
    top_limit = int(input("type your number: "))
    output = ""

    while top_limit > 1:
        top_limit -= 1
        top_limit_string = str(top_limit) + " "
        output += top_limit_string

    print(f"checker: {output}")

    counter = 0
    for i in range(len(output)):
        counter += 1
        if output[i] == " ":
            continue
        else:
            print(output[:-counter])
except:
    print("error occurs, type only integer number")
'''

print("-"*50)

# Soal 7
print("soal 7")
try:
    baris = 5
    triangle = ""
    for i in range(1, baris+1):
        counter = 1
        space = 8
        for j in range(1, i+1):
            triangle = (' ' * space + '* ' * counter)
            space -= 2
            counter += 2
        print(triangle)

    # for i in range(1, baris + 1):
    #     counter = 9
    #     space = 0
    #     for j in range(1, i+1):
    #         triangle = (' ' * space + '* ' * counter)
    #         space += 2
    #         counter -= 2
    #     print(triangle)
except:
    print("error occurs, type only integer number")


'''
try:
    # string = ""

    # x = int(input("Masukkan angka :"))
    # bar = x
    # # Looping Baris
    # while bar >= 0:
    #     # Looping Kolom Spasi Kosong
    #     kol = bar
    #     while kol > 0:
    #         string = string + "   "
    #         kol = kol - 1
    #     # Looping Kolom Bintang Sisi Kiri
    #     kiri = 1
    #     while kiri < (x - (bar-1)):
    #         string = string + " * "
    #         kiri = kiri + 1
    #     # Looping Kolom Bintang Sisi Kanan
    #     kanan = 1
    #     while kanan < kiri - 1:
    #         string = string + " * "
    #         kanan = kanan + 1

    #     string = string + "\n\n"
    #     bar = bar - 1

    # print(string)

    #     string = ""
    #     x = int(input("type your number: "))
    #     bar = x

    #     for i in range(bar):
    #         # empty space
    #         space = bar
    #         for i in range(x):
    #             string += ""
    #             space -= 1

    #         # left side star
    #         left = 1
    #         for i in range(x - (bar-1)):
    #             string += " * "
    #             left += 1

    #         # right side star
    #         for i in range(left + 1):
    #             string = string + " * "

    #         string += '\n\n'
    #         bar = bar - 1
    #     print(string)

    # except:
    #     print("error occurs, type only integer number")
'''

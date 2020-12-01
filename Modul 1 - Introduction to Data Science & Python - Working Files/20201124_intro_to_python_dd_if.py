'''
# Soal 1
print("Soal 1")
day = ['senin', 'selasa', 'rabu', 'kamis', "jum'at", 'sabtu', 'minggu']

try:
    day_input = input("enter the day: ").lower()
    counter = int(input("enter the counter: "))

    if day_input in day:
        print("day exists")

        # check index
        index = day.index(day_input)
        appointed_day = index + counter

        if -len(day) <= appointed_day <= len(day) - 1:
            print(
                f"'{counter}' days from '{day_input}' is '{day[appointed_day]}'\n")
        else:
            if appointed_day > (len(day) - 1):
                while appointed_day > (len(day) - 1):
                    appointed_day -= 7
            elif appointed_day < -len(day):
                while appointed_day < -len(day):
                    appointed_day += 7
            else:
                print('error')

            print(
                f"'{counter}' days from '{day_input}' is '{day[appointed_day]}'\n")
    else:
        print("day doesn't exist\n")
except:
    print("counter should be integer\n")

print("*" * 50)
'''

# Soal 2
# print("Soal 2")

# try:
#     text_input = input("enter the words: ").lower()

#     if len(text_input) > 1:
#         if text_input[:] == text_input[::-1]:
#             print("this is a palindrome\n")
#         else:
#             print("this is not a palindrome\n")
#     else:
#         print("the input must be longer than 1 character")
# except:
#     print('error occurs, input should be a text')

# Soal 3
# print("Soal 3")
# number_input = int(input("enter the number: "))
# result = ((number_input - 93) // 100) + (93 * 100)
# print(result)


# Soal 4
# print("Soal 4")
try:
    input1 = int(input("enter the number: "))
    input2 = int(input("enter the number: "))

    result = ""
    if len(str(input1)) == 2 and len(str(input2)) == 2:
        result = (input1 * (10 ** len(str(input1)))) + input2
        print(result)
    else:
        print("input should be 2 digit and not negative")
except:
    print("input should be integer")

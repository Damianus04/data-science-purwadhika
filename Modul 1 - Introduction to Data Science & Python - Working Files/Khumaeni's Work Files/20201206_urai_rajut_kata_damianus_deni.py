# 1) URAI Function
def urai(text):
    output = ""

    for i, j in enumerate(text):
        output = output + text[:i+1]

    return output


text1 = "Code"
text2 = "Python"
text3 = "Purwadhika"

print(f"{text1} --> {urai(text1)}")
print(f"{text2} --> {urai(text2)}")
print(f"{text3} --> {urai(text3)}")


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


text4 = "CCoCodCode"
text5 = "PPyPytPythPythoPython"
text6 = "PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"

print(f"{text4} --> {rajut(text4)}")
print(f"{text5} --> {rajut(text5)}")
print(f"{text6} --> {rajut(text6)}")

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

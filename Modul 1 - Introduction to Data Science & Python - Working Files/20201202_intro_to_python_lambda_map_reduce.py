# Berapa jumlah total bilangan ganjil yang telah dipangkatkan 3 dari rentang angka 1-200

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

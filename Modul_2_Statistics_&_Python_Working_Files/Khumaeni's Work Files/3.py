# Data Collection - Acquisition

# Database ==> Front Page => Coding Python ==> statis

# => Data Dinamis
# Database ==== API ===== Front Page
#                ||
#                Coding Python

# ############################ API
# API ==>

import requests
import json

# url = "https://jsonplaceholder.typicode.com/users"
# data = requests.get(url)
# output = data.json()

# # print(output[2])
# # print(len(output))
# for i in range(len(output)):
#     print(f"Name: {output[i]['name']} \nEmail: {output[i]['email']}")

# Program Konversi Mata Uang:
# Menu:
# 1. IDR to Mata Uang Asing
# 2. Mata Uang Asing to IDR

# Pilihan 1:
# - masukkan nama bank
# - masukkan mata uang asing: usd/jpy/gbp dll
# - masukkan nilai rupiah: 500000

# Output:
# nilai uang anda 1000 rupiah dalam usd adalah (nilai konversi)
# -> nuker rupiah ke dolar pakai nilai jual
# -> nuker dolar ke rupiah pakai nilai beli

# Pilihan 2:
# - masukkan nama bank
# - masukkan mata uang asing: usd/jpy/gbp dll
# - masukkan nilai rupiah: 500000

# Output:
# nilai uang anda 50 usd dalam rupiah adalah (nilai konversi)

# token = "bDSGqWmkLACiWbV9oXYuqn0MDn5wSEn0EEyjZ8Nx"
# option = input(
#     """choose your option:
#     1) IDR to Foreign Currency
#     2) Foreign Currency to IDR
#     --> """)

# if option == "1":
#     bank = input("choose the bank: ").lower()
#     currency = input("choose the currency: ").lower()
#     amount = int(input("type your amount: "))

#     url = f"https://api.kurs.web.id/api/v1?token={token}&bank={bank}&matauang={currency}"
#     data = requests.get(url)
#     output = data.json()
#     rate = output['jual']

#     output = amount / rate

#     print(
#         f"in bank: '{bank}', '{amount}' IDR is '{output}' '{currency.upper()}'")
# elif option == '2':
#     bank = input("choose the bank: ").lower()
#     currency = input("choose the currency: ").lower()
#     amount = int(input("type your amount: "))

#     url = f"https://api.kurs.web.id/api/v1?token={token}&bank={bank}&matauang={currency}"
#     data = requests.get(url)
#     output = data.json()
#     rate = output['beli']

#     output = amount * rate

#     print(
#         f"in bank: '{bank}', '{amount}' '{currency.upper()}' is '{output}' IDR ")


# Prakiraan Cuaca
# url = https://openweathermap.org/current
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
Input:

key = "479f8bc4202658a493ab6435aa6c0f72"
host = "api.openweathermap.org"
city = input("select a city: ")
url = f"https://{host}/data/2.5/weather?q={city}&appid={key}"

data = requests.get(url)
weather = data.json()

print(weather)

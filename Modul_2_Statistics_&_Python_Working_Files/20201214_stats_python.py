'''

from bs4 import BeautifulSoup
import requests
import json
Data Analytics == > Data Analyst

EDA - Exploratory Data Analysis(Data Analysis & Data Vis)
Explanatory Data Analysis
- Data Collection
- Web Scrapping
- Rest API
- Database

- Data Analysis
- Basic Stats == > Descriptive Analysis/Stats
- Pandas
- Numpy

- Data Visualization
- Matplotlib
- seaborn
- folium
- Tableau

- Dashboard
- Flask


Data Collection - Data Acquisition

---Data Sources

- Internal
==> Data dari perusahaan (Bisa dari bagian sendiri maupun lintas dept.)
- ERP => Enterprise Resource Planning --> Sistem terintegrasi ==> Front End
- Database ==> Back End

- External
- Data Dari Supplier
atau sumber lain yg legal.

Web Publik ==> Website yg di open untuk Publik 

Front End ---> Halaman yg bisa kita lihat as user 

Database ---------> Front End (Front Page) -- HTML Page 

==> Web Scrapping

Database ----> Frond End (Html Page) ==> Scrapped
- Teknik Mengekstraksi Data dari website yg akan kita simpan di lokal kita bisa berupa Spreadsheet, csv, db, json, dll
- Suatu Teknik Automatisasi pengambilan data dari internet yg tidak atau semi terstruktur menjadi terstruktur (Tabel)
- Digunakan untuk halaman yg Datanya Statis

==> Langkah 
- Tentukan dulu Data yg akan diambil 
- Tentukan url (website nya)
- Lihat struktur website - Inspect Element, view Page Source, Postman
- Coding ==> Scrap data termasuk simpan ke lokal 
'''


# BeautifulSoup
# Requests

# py -m pip install beautifulsoup4
# py -m pip install requests

# pip install beautifulsoup4
# pip install requests

# File HTML Offline
# Beautifulsoup


# BeautifulSoup()
# import bs4

# bs4.BeautifulSoup()

# url = "http://127.0.0.1:5500/4DOMEvents.html"

# Out = BeautifulSoup(open(url, 'r'), "html.parser")
# # r => read

# print(Out)

# Web Scrapping
# url = "http://127.0.0.1:5500/4DOMEvents.html"

# web = requests.get(url)

# # Out = BeautifulSoup(open(url, 'r'), "html.parser")
# Out = BeautifulSoup(web.content, 'html.parser')

# print(Out.title.text)

# for i in Out.find_all('p'):
#     print(i.text)

# for i in Out.find_all('li', class_='b-list'):
#     print(i.text)


# print(Out.prettify)
# print(Out.title)
# print(Out.title.text)
# tag html
# <.>Data yg kita cari</.>

# print(Out.h3)
# print(Out.h3.text)

# print(Out.h2.text)

# print(Out.p.text)
# print(Out.b.text)

# print(Out.strong.text)

# print(Out.ul.text)
# print(Out.li)
# print(Out.li.text)

# for i in Out.find_all('li'):
#     print(i.text)

# tamu = []
# for i in Out.find_all('li', class_ = "Orang"):
#     tamu.append(i.text)

# print(tamu)


# - JSON ==> JavaScript Object Notation

# member = [{
#     "nama": "Rudi",
#     "usia": 20,
#     "kota": "bandung"
# }]


# Menulis file Json
# with open("latihan.json", "w") as file:
#     json.dump(member, file)

# print("File Created")
# w = write => nulis
# dump = fungsi untuk menulis file json

# r = read => ngebaca
# load = fungsi untuk membaca file json

# Membaca File Json
# with open("latihan.json", "r") as file:
#     Output = json.load(file)

# print("Data Loaded")
# print(Output)


# File HTML Online
# BeautifulSoup
# Requests

from bs4 import BeautifulSoup
import requests
# # --- GET dan POST ==> Request

# url = "http://127.0.0.1:5500/contoh.html"

# web = requests.get(url)

# Out = BeautifulSoup(web.content, 'html.parser')

# print(Out.h1.text)

# print(Out.p.text)

# print(Out.strong.text)

# tamu = []
# for i in Out.find_all('li', class_ = "Orang"):
#     tamu.append(i.text)

# print(tamu)

# employee = []
# for i in Out.find_all('li', id= "Person2"):
#     employee.append(i.text)
# print(employee)

### Latihan - Tugas
# Lakukan Web-Scrapping dari :
# http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/

# Daftar Ultraman dan Daftar Monster
# Nama-Ultraman dan No nya, ==> 01. Ultraman
# Nama-Monster dan No nya, ==> 73. Judah Spectre

# Export ke dalam File JSON

# Format Isi untuk File Json :
# [{"Ultraman" : {"01" : "Ultraman", "02": "Ultra Seven".....}
# "Monster" : {"01" : "Alien Baltan", "02" : "Gomora"....}}]

# Email :
# purwadhika.jcds@gmail.com


# Data Collection - Acquisition

# Database ==> Front Page => Coding Python ==> statis

# => Data Dinamis
# Database ==== API ===== Front Page
#                ||
#                Coding Python

# ############################ API
# API ==>


# url = "https://jsonplaceholder.typicode.com/users"
# data = requests.get(url)
# output = data.json()

# # print(output[2])
# # print(len(output))
# for i in range(len(output)):
#     print(f"Name: {output[i]['name']} \nEmail: {output[i]['email']}")


# TUGAS
# 1. Program Konversi Mata Uang:
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

token = "bDSGqWmkLACiWbV9oXYuqn0MDn5wSEn0EEyjZ8Nx"
option = input(
    """choose your option:
    1) IDR to Foreign Currency
    2) Foreign Currency to IDR
    --> """)

system = ''
while system != 'y':
    if option == "1":
        bank = input("choose the bank: ").lower()
        currency = input("choose the currency: ").lower()
        amount = int(input("type your amount: "))

        url = f"https://api.kurs.web.id/api/v1?token={token}&bank={bank}&matauang={currency}"
        data = requests.get(url)
        output = data.json()
        rate = output['jual']

        output = amount / rate

        print(
            f"in bank: '{bank}', '{amount}' IDR is '{output}' '{currency.upper()}'")
    elif option == '2':
        bank = input("choose the bank: ").lower()
        currency = input("choose the currency: ").lower()
        amount = int(input("type your amount: "))

        url = f"https://api.kurs.web.id/api/v1?token={token}&bank={bank}&matauang={currency}"
        data = requests.get(url)
        output = data.json()
        rate = output['beli']

        output = amount * rate

        print(
            f"in bank: '{bank}', '{amount}' '{currency.upper()}' is '{output}' IDR ")
    else:
        print("please select '1' or '2'")

    system = input('''do you want to repeat: 
                    --> yes (y)
                    --> no (n)''')

# 2.  Prakiraan Cuaca
# url = https://openweathermap.org/current
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# Input: Masukkan nama kota:
# Output:

# kota yang anda pilih adalah: .....
# suhu: ... (celcius)
# keadaan cuaca: ... berawan ...
# koordinat kota anda: lat ... long ...
# humidity level: ....
# kecepatan angin: ...

# kalau kota tidak ada:
# kota yang anda masukkan tidak terdaftar

# format kota yang anda masukkan salah
# key = "479f8bc4202658a493ab6435aa6c0f72"
# host = "api.openweathermap.org"
# city = input("select a city: ")
# url = f"https://{host}/data/2.5/weather?q={city}&appid={key}"

# data = requests.get(url)
# weather = data.json()

# print(weather)


# Zomato
# import requests

# key = "d144413ae947e1fca6f92d6f043e82eb"
# cat = "/categories"
# city = "/cities"
# host = "https://developers.zomato.com/api/v2.1"

# head = {'user-key': key}

# url1 = host + cat
# url2 = host + city

# data1 = requests.get(url1, headers=head)
# data2 = requests.get(
#     url2, headers={"user-key": "d144413ae947e1fca6f92d6f043e82eb"})

# output1 = data1.json()
# category1 = output1['categories']

# list_cat = []

# for i in range(len(category1)):
#     list_cat.append(category1[i]['categories']['name'])

# print(list_cat)


# LATIHAN - TUGAS
# gunakan API zomato

# selamat datang di zomato apps:
# silahkan pilih opsi:
# 1. cari resto
# 2. daily menu

# opsi 1:
# mencari restoran di kota tertentu
# input: masukkan nama kota:
# masukkan jumlah restoran yang akan ditampilkan

# output:
# - nama restoran: ...
# - establishment name: ...
# - cuisine name: ...
# - alamat: ...
# - no telpon: ...
# - rating: ... (angka)
# - review: ... (angka)

# opsi 2:
# daily menu - menu harian resto
# input:
# - masukkan nama kota
# - masukkan nama resto:
# - jumlah menu yang akan ditampilkan:

# output:
# daily menu di restorean xxx adalah...


# # POKE API
# # https://pokeapi.co/
# masukkan nama pokemon:

# output:
# - nama pokemon:
# - HP: ...
# - attack: ...
# - defense: ...
# - speed: ...
# - type: ...
# - image: ... url image foto pokemon ...
# - ability name:
# 1. ...
# 2. ...
# 3. ...
# 4. ...

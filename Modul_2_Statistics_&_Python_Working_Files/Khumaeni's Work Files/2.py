'''
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

###File HTML Offline
# Beautifulsoup 

from bs4 import BeautifulSoup

# BeautifulSoup()
# import bs4

# bs4.BeautifulSoup()

url = "contoh.html"

Out = BeautifulSoup(open(url, 'r'), "html.parser")
# r => read

# print(Out)
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

member = [{
    "nama" : "Rudi",
    "usia" : 20,
    "kota" : "bandung"
}]

import json

## Menulis file Json
# with open("latihan.json", "w") as file:
#     json.dump(member, file)

# print("File Created")
# w = write => nulis
# dump = fungsi untuk menulis file json 

# r = read => ngebaca
# load = fungsi untuk membaca file json 

## Membaca File Json
# with open("latihan.json", "r") as file:
#     Output = json.load(file)

# print("Data Loaded")
# print(Output)



### File HTML Online
# BeautifulSoup
# Requests 

from bs4 import BeautifulSoup
import requests
# --- GET dan POST ==> Request 

url = "http://127.0.0.1:5500/contoh.html"

web = requests.get(url)

Out = BeautifulSoup(web.content, 'html.parser')

print(Out.h1.text)

print(Out.p.text)

print(Out.strong.text)

tamu = []
for i in Out.find_all('li', class_ = "Orang"):
    tamu.append(i.text)

print(tamu)

employee = []
for i in Out.find_all('li', id= "Person2"):
    employee.append(i.text)
print(employee)

### Latihan - Tugas
Lakukan Web-Scrapping dari :
http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/

Daftar Ultraman dan Daftar Monster
Nama-Ultraman dan No nya, ==> 01. Ultraman
Nama-Monster dan No nya, ==> 73. Judah Spectre

Export ke dalam File JSON

Format Isi untuk File Json :
[{"Ultraman" : {"01" : "Ultraman", "02": "Ultra Seven".....}
"Monster" : {"01" : "Alien Baltan", "02" : "Gomora"....}}]

Email :
purwadhika.jcds@gmail.com 
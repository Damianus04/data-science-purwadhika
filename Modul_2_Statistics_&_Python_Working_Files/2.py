import json
# from bs4 import BeautifulSoup


# url = "4DOMEvents.html"

# Out = BeautifulSoup(open(url, 'r'), "html.parser")

# print(Out.title)


# member = [{
#     "nama": "Rudi",
#     "usia": 20,
#     "kota": "bandung"
# }]

# # menulis file json
# with open("exercise.json", "w") as file:
#     json.dump(member, file)

# print("file created")
# w = write
# dump = fungsi untuk menulis file json


# membaca file json
# with open("exercise.json", "r") as file:
#     output = json.load(file)

# print("data loaded")
# print(output)
# r = read => ngebaca
# load = fungsi untuk membaca file json

from bs4 import BeautifulSoup
import requests
# --- GET dan POST --> Request

url = "http://127.0.0.1:5500/Modul_2_Statistics_&_Python_Working_Files/4DOMEvents.html"

web = requests.get(url)

Out = BeautifulSoup(web.content, 'html.parser')

print(Out.h1.text)


# Latihan - Tugas
# lakukan web-scrapping dari:
# url = "http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/"

# daftar ultraman dan daftar monster
# nama-ultraman dan no nya, ==> 01. Ultraman
# nama-monster dan nonya, ==> 73. Judah Spectre

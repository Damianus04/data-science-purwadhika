### Data Collection - Acquisition
'''
Database ========> Front Page => Coding Python ==> Statis ==> Web Scraping 


=> Data Dinamis 
Database ===== API  =======> Front Page
                ||
                Coding Python

#################### API
API ==> Application Programming Interface 
Aplikasi A      API      Aplikasi B
                         Aplikasi D 
                         Aplikasi C

################### REST API 

REST API => Representational State Transfer API 

Database ===== REST API  =======> Front Page ==> Via Web Scrapping 
                ||
                Coding Python ==> Via REST API 

## REST API 
- Data Dinamis ==> Contoh Cuaca, mata uang (konversi)
- Terkoneksi dg Internet 
- API itu dibuat oleh Developer 
- Hanya dapat digunakan untuk web-web tertentu yg memang memiliki API (Telah disediakan oleh Developer) 
- Format API berbeda untuk masing-masing Web, tergantung Developer nya.
- Limited Access ==> Terbatas tergantung Developer 
- Format Data umumnya berbentuk Json 

Request ==> GET 
Response ==> Respon dari Server 

## Langkah Collect Data via API
- Tentukan Data yg dibutuhkan 
- Tentukan Web yg menyediakan Data tsb
- Pastikan Web memiliki API   
- Pastikan Data dapat disediakan melalui API 
- Ketahui Format Akses API 
- Coding 


Package ==> Requests 
'''

import requests
'''
url = 'https://jsonplaceholder.typicode.com/users'

data = requests.get(url)

output = data.json()

# print(output[2])
# print(len(output))

for i in range(10):
    print(f"Nama - {output[i]['name']}; Email - {output[i]['email']}")
'''


################################ Konversi Mata Uang
### https://api.kurs.web.id

# 7CEbMdSUFrBLTmW1WMk9ywDZuqSj4BzKlWlDVznL
'''
# URL = "{API_ENDPOINT}/api/v1?token={TOKEN}&bank={KODE_BANK}&matauang={MATA_UANG}"
bank = input("masukkan bank : ")
matauang = input("masukkan mata uang : ")

url = f"https://api.kurs.web.id/api/v1?token=7CEbMdSUFrBLTmW1WMk9ywDZuqSj4BzKlWlDVznL&bank={bank}&matauang={matauang}"

data = requests.get(url)
output = data.json()

print(output['jual'])
print(output['beli'])

########################## Konversi Mata Uang
Buat Program untuk Konversi mata uang 

Menu :
1. IDR to Mata Uang Asing 
2. Mata Uang Asing to IDR 

Pilihan 1 :
- Masukkan Nama Bank 
- Masukkan Mata Uang Asing : USD/JPY/GBP dll 
- Masukkan Nilai Rupiah : 500000

Output :
Nilau uang anda ... Rupiah dalam ..(mata uang asing)... adalah .... (nilai konversi) 

Pilihan 2:

- Masukkan Nama Bank 
- Masukkan Mata Uang Asing : USD/JPY/GBP dll 
- Masukkan Nilai uang anda : 50

output:
Nilau uang anda .50 usd.. (Mata uang asing) dalam rupiah . adalah .... (nilai konversi)... 
'''

########################################## Open WeatherMap ## Prakiraan Cuaca
### https://openweathermap.org/

# api.openweathermap.org/data/2.5/weather?q=London&appid={API key}

key = '3a18ccca6a337aa57302cc46a2907609'
host = "api.openweathermap.org"
kota = input("Masukkan Nama Kota : ")

url = f"https://{host}/data/2.5/weather?q={kota}&appid={key}"

data = requests.get(url)
cuaca = data.json()

print(cuaca)

#### Latihan Prakiraan Cuaca

Input : Masukkan Nama Kota : 

Output :

Kota yang anda pilih adalah : .....
Suhu : .... (Celcius)
Keadaan cuaca : ..... berawan ...
Koordinat Kota anda : Lat .... Long ...
Humidity Level : ....
Kecepatan Angin : .....

Kalau Kota tidak ada : 
Kota yang anda masukkan tidak terdaftar 

Format Kota yang anda masukkan salah 

## Gunakan API OpenweatherMap
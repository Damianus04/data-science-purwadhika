# Untuk mengkoneksikan Database MongoDB dengan Program Python
# dibutuhkan Package
# pymongo


# ###Install Package pymongo
# - py -m pip install pymongo
# - pip3 install pymongo 

import pymongo
# print("Install Success")

# Database (Server) ======= Client ==> Harus mengetahui Nama Server atau IP server 
# Harus tau Nama Server 

# Jika MongoDB Tidak di set sebagai Services (Autorun), maka server harus dinyalakan 

# ## Cara Menyalakan - Mengaktifkan Server
# Buka Command Prompt(Terminal)
# Masuk ke Path Server : C:\Program Files\MongoDB\Server\4.2\bin
# Ketik : mongod 

# ### Definisikan Lokasi Server
# mongodb://Nama server:port/

dburl = 'mongodb://localhost:27017'  ## Mendefiniskan Lokasi Server (Lokal) dan Port (Default : 27017)

# 27017 : Port Default dari MongoDB 
# Localhost : Karena DB diinstall di PC/Device Client (Lokal)

#### Definisikan Client

myMongo = pymongo.MongoClient(dburl) ### Mendefinisikan Client yg akan terkoneksi dengan Server(DB) yg telah didefiniskan sebelumnya

# print("Connection Success")


### Show Database ==> Untuk melihat Isi Database di dalam Server
dbs = myMongo.list_database_names()

# print(dbs)

### Untuk Melihat Collections ==>Kita harus masuk / Memilih Database terlebih dahulu

myDB = myMongo['Purchasing']  ### Memilih Database
# myDB1 = myMongo['Finance']  ### Jika akan mengakses lebih dari satu Database

List_Col = myDB.list_collection_names()  ### Untuk melihat Collections di dalam Database Purchasing

# print(List_Col)


### Memilih / Menggunakan Collection
myEmployee = myDB['Employee']  ### Mengaktifkan/memilih Collection Employee
# myAset = myDB['Aset'] ## Mengaktifkan Collections Aset


###### Melihat Data dalam Collections (Read)
## Hasil dari .find() berupa Object, sama seperti map atau filter
## Sehingga perlu dikonversi agar bisa dibaca

All_Data = list(myEmployee.find())  ### Menampilkan Seluruh data di dalam Collections
# print(All_Data)


### Looping Data yg telah dikonversi
# for i in All_Data:
#     print(i['Nama'])

# ### Untuk Mengakses Seluruh Data
# - Gunakan Konversi
# - Looping Data tanpa konversi 

## Looping data tanpa konversi

# for i in myEmployee.find():
#     print(i)


########################### Membuat Database & Collection Baru

# print(dbs)

newDB = myMongo['Marketing'] 
# ### Memiliki 2 fungsi
# - Jika Database sudah ada di dalam server, maka DB tersebut akan dipilih dan diaktifkan (Contoh DB Purchasing)
# - Tapi, Jika Database Belum ada/Tidak Ada, maka DB tersebut akan dibuat 
# - Berlaku juga untuk Collections 

newCol = newDB['Karyawan'] ## Membuat Collection Karyawan

# print(dbs)
### Database baru tidak akan tampil, Jika belum ada data di dalam Collections ###

###### Memasukkan Data ke dalam Collections (Create)

data = {
    "NIK" : "123AB",
    "Nama" : "Ricky",
    "Kota" : "Jakarta",
    "Usia" : 24
}

# newCol.insert_one(data)  ### Memasukkan Data ke dalam Collections (newCol)

# print("Data Submitted")
# print(dbs)

# for i in newCol.find(): ## Untuk melihat Isi data di dalam Collections
#     print(i)

data_1 = {
    "NIK" : "124AC",
    "Nama" : "John",
    "Kota" : "Bandung",
    "Usia" : 26
}

# x = newCol.insert_one(data_1)
# x.inserted_id  ==> Untuk memunculkan ID ketika data awal baru dimasukkan 
# print(f"Data Submitted, With ID : {x.inserted_id}")
# for i in newCol.find(): ## Untuk melihat Isi data di dalam Collections
#     print(i)


### Mengakses data dg Kondisi tertentu
## Isi Collections Employee
# { "_id" : ObjectId("5fda1e90212bd840db6fec1c"), "Nama" : "Rosi", "Kota" : "Jakarta", "Gaji" : 15000000, "Divisi" : "Data Management", "Umur" : 25 }
# { "_id" : ObjectId("5fda1e90212bd840db6fec1d"), "Nama" : "Sisi", "Usia" : 27, "Kota" : "Bandung", "Gaji" : 20000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fda1e90212bd840db6fec1e"), "Nama" : "Rosi", "Kota" : "Malang", "Gaji" : 12000000, "Divisi" : "Data Management", "Umur" : 20 }
# { "_id" : ObjectId("5fda1e90212bd840db6fec1f"), "Nama" : "Andre", "Usia" : 25, "Kota" : "Jakarta", "Gaji" : 17000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fda1e90212bd840db6fec20"), "Nama" : "Joni", "Usia" : 23, "Kota" : "Bandung", "Gaji" : 13000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fda1e90212bd840db6fec21"), "Nama" : "Adam", "Usia" : 28, "Kota" : "Malang", "Gaji" : 20000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fdb5bcffb746baf2e3df24e"), "Nama" : "Yogi", "Usia" : 30, "Kota" : "Malang", "Gaji" : 16000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fdb5bcffb746baf2e3df24f"), "Nama" : "Cecil", "Usia" : 26, "Kota" : "Bandung", "Gaji" : 15000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fdb5bcffb746baf2e3df250"), "Nama" : "Andre", "Usia" : 27, "Kota" : "Jakarta", "Gaji" : 17000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fdb5bcffb746baf2e3df251"), "Nama" : "Andi", "Usia" : 28, "Kota" : "Bandung", "Gaji" : 25000000, "Divisi" : "Data Management" }
# { "_id" : ObjectId("5fdb6182fb746baf2e3df252"), "Nama" : "Mike", "Kota" : "Bekasi", "Gaji" : 17000000, "Divisi" : "Data Management" }


kondisi = {"Nama" : "Cecil"}

Cari = myEmployee.find(kondisi)

# for i in Cari:
#     print(i)

## query : db.employee.find({"Nama" : "Cecil"})

####### Memasukkan Data Berdasarkan User Input
'''
col_Baru = newDB['Barang'] ## Collections baru di dalam DB marketing

kode = input("Masukkan Kode Barang : ")
nama = input("Masukkan Nama Barang : ")
harga = float(input("Masukkan Harga Barang : "))
stok = int(input("Masukkan Stok Barang : "))

new_data = {
    "Kode" : kode,
    "Nama" : nama,
    "Harga" : harga,
    "Stok" : stok
}

x = col_Baru.insert_one(new_data)

print(f"Data Berhasil diInput dengan ID : {x.inserted_id} ")

print("="*50)

print("Keseluruhan Barang : ")
for i in col_Baru.find():
    print(i)
'''

##### Memasukkan Banyak Data Sekaligus
col_2 = newDB["Seragam"] 
'''
col_2 = newDB["Seragam"]  ### Memasukkan/Membuat Collection Baru (Seragam) di dalam Database lama (Marketing)

DATA = [
    {"Jenis" : "Celana Panjang", "Stok" : 30},
    {"Jenis" : "Kemeja", "Stok" : 25},
    {"Jenis" : "Kaos", "Stok" : 15},
    {"Jenis" : "Sepatu", "Stok" : 20}
]


col_2.insert_many(DATA)

print("Data Saved")
print("="*100)

for i in col_2.find():
    print(i)

'''

#### Mengakses Data Collections dengan Kondisi Tertentu
# for i in myEmployee.find():
#     print(i)

### Akses menggunakan syntax Membership (IN)
'''
Kota = ["Jakarta", "Bandung"]
kondisi = {"Kota" :{"$in" : Kota}}

y = myEmployee.find(kondisi)

for i in y:
    print(i)
'''

#### Conditional - Logical Condition

## Operator OR
## Menampilkan Data yg memenuhi Minimal Salah satu Kondisi yg ditentukan 

# Alt 1
# Kondisi = {"$or" : [{"Gaji" : 15000000}, {"Kota" : "Malang"}] }

# # z = myEmployee.find(Kondisi)
# # for i in z:
# #     print(i)

# # Alt 2
# operator = "$or"
# Kondisi1 = {"Gaji" : 15000000}
# Kondisi2 = {"Kota" : "Malang"}

# query = {operator : [Kondisi1, Kondisi2] }

# z = myEmployee.find(query)

# for i in z:
#     print(i)

### Operator AND
## Menampilkan Data yg memenuhi SELURUH Kondisi yg ditentukan 
# Alt 1
# Kondisi = {"$and" : [{"Gaji" : 12000000}, {"Kota" : "Malang"}] }

# z = myEmployee.find(Kondisi)
# for i in z:
#     print(i)

# # Alt 2
# operator = "$and"
# Kondisi1 = {"Gaji" : 12000000}
# Kondisi2 = {"Kota" : "Malang"}

# query = {operator : [Kondisi1, Kondisi2] }

# z = myEmployee.find(query)

# for i in z:
#     print(i)


# query = {"Kota" : {"$ne" : "Malang"}}  #### ne = Not Equal = Tidak sama dengan
# z = myEmployee.find(query)

# for i in z:
#     print(i)

######################## MENGUPDATE DATA

##### Ketika yg akan diupdate adalah Value
# for i in col_2.find():
#     print(i)
'''
{'_id': ObjectId('5ff5c9e72f937d6e418df40b'), 'Jenis': 'Celana Panjang', 'Stok': 30}
{'_id': ObjectId('5ff5c9e72f937d6e418df40c'), 'Jenis': 'Kemeja', 'Stok': 25}
{'_id': ObjectId('5ff5c9e72f937d6e418df40d'), 'Jenis': 'Kaos', 'Stok': 15}
{'_id': ObjectId('5ff5c9e72f937d6e418df40e'), 'Jenis': 'Sepatu', 'Stok': 20}
'''
Data = {"Jenis" : "Kemeja"} ## Kondisi Data yg akan diupdate
new_val = {"$set" : {"Stok" : 50}} ## Value Baru yg akan diupdate

# col_2.update_one(Data, new_val)

# for i in col_2.find():
#     print(i)


### Mengupdate Banyak Data Sekaligus
# Data = {} ## Kondisi Data yg akan diupdate dikosongkan == Seluruh Data
# value_baru = {"$set" : {"Kondisi" : "BNIB"} }

# col_2.update_many(Data, value_baru)
# print("Data Updated")

# for i in col_2.find():
#     print(i)

### Menghapus Property
# Data = {"Jenis" : "Kaos"}
# new_val = {"$unset" : {"Kondisi" : True}}
# col_2.update_one(Data, new_val)

# print("data updated")

# for i in col_2.find():
#     print(i)

#### Mengubah Property
# Data = {"Stok" : 50}
# new_val = {"$rename" : {"Jenis" : "Nama"}}

# col_2.update_one(Data, new_val)

# for i in col_2.find():
#     print(i)

### Hapus Data
Kondisi = {"Jenis" : "Sepatu"}
col_2.delete_one(Kondisi)

for i in col_2.find():
    print(i)

### Hapus Seluruh Data
Kondisi = {}

col_2.delete_many({})

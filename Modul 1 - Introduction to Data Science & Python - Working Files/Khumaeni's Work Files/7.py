##### Tuple == Mirip dengan List, Tetapi Element nya Immutable
# Immutable ==> Tidak bisa diupdate
# tuple_A = ()
# tuple_B = tuple(data)
tuple_C = 2, 4, "senin", "selasa"  ## Data hanya dipisahkan dg Koma tanpa Tanda kurung

hari = ("senin", "selasa", "rabu", "kamis")

### Create - Tambah Data ==> Tidak dapat dilakukan
# hari.append("kamis")  ## Tidak bisa menambahkan data baru ke dalam Tuple
# hari.extend("jumat")  ## Tuple tidak memiliki fungsi/attribut Extend dan Append untuk menambah Data

## Update - Ubah Data ==> Tidak dapat dilakukan
# hari[0] = "kamis" ## Data dalam tuple tidak bisa diubah

## Delete - Hapus data ==> Tidak bisa dilakukan
# hari.remove("senin")
# hari.pop()

## Read - Membaca Data ==> Indexing dan Slicing dapat dilakukan
## Aturan penggunaaan sama dengan Indexing dan Slicing pada List
'''
print(hari[0])
print(hari[:2])
print(hari[1])
print(hari[-1])

print(hari.index("rabu"))  ## Fungsi Index dapat digunakan

angka = (35, 71, 5, 100, 250, 90, 45, 5)
print(angka.count(5))  ## Fungsi COunt dapat digunakan
# angka.sort()  ## Tuple tidak memiliki fungsi Sort
print(angka)
'''
## Tuple hanya memiliki 2 fungsi - Count dan Index dan len

### Packing - Unpacking

# --- Packing ---

## Proses memasukkan beberapa data ke dalam Tuple
# user = ("Andi", 25, "Jakarta")
user = "Andi", 25, "Jakarta" # Format Lain
'''
# ---- Unpacking
print(len(user))
Nama, Usia, Kota = user  ## Meng-Assign, Setiap elemen dari Tuple ke dalam Variabel yg berbeda
## Jumlah Variabel Harus Sama dengan Jumlah Elemen dalam Tuple
# 1, 2,3,4= train_test(......)
print(Nama)
print(Usia)
'''
# Konsep Packing - UnPacking sebenarnya mengadopsi atau serupa dengan Konsep Multiple Assignment

a, b, c = 70, 85, 90

data = 70, 80, 85, [89, 90, 78, (56, 87, 90, ["senin", "selasa", (True, False)])]

# print(type(data))

# print(data.index([89, 90, 78, (56, 87, 90, ["senin", "selasa", (True, False)])]))

# print(data[3])

# print(data[3].index((56, 87, 90, ["senin", "selasa", (True, False)])))

# print(data[3][3].index(["senin", "selasa", (True, False)]))

# print(data[3][3][3])


# print(data[3][3][3].index((True, False)))

# print(data[3][3][3][2])

# print(data[3][3][3][2].index(False))

# print(data[3][3][3][2][1])

###### SET
list_A = []
tuple_A = ()
set_A = {}
set_B = set()

### Unordered List, Unique, No Indexing
## Set === HIMPUNAN 
# avanza = 10
# yaris = 50
# xenia = 30
# jazz = 10

mobil = ["avanza", "avanza", "yaris", "xenia", "yaris", "jazz", "avanza", "avanza", "yaris", "xenia", "yaris", "jazz", "avanza", "avanza", "yaris", "xenia", "yaris", "jazz"]
print(mobil)
set_mobil = {"avanza", "avanza", "yaris", "xenia", "yaris", "jazz", "avanza", "avanza", "yaris", "xenia", "yaris", "jazz", "avanza", "avanza", "yaris", "xenia", "yaris", "jazz"}
print(type(set_mobil))

print(set_mobil)


### Tugas 
1.
Hari = ['senin', 'selasa', 'rabu', 'kamis', "jum'at", 'sabtu', 'minggu']

input : 
"Masukkan nama Hari : " SEniN
"Masukkan Jumlah : " 100 (Nilai Harus Integer) Jika Bukan Integer Keluar Notifikasi : ...
-2
Output :
"100 hari dari hari ... (senin) ... adalah hari ...."
"-2 hari dari hari ... (senin) ... adalah hari ....(sabtu)"
"3 hari dari hari ... (senin) ... adalah hari ....(kamis)"
Kondisi :
- Tidak Case Sensitive
- Ada Pengecekan Hari : Tidak ada Nama Hari 
- Jumlah angka Harus Integer (bisa positif maupun Negatif)

2. 
Palindrome 
katak = katak 
Level = level 
Madam = madam 
Noon = Noon 
input : Masukkan kata : ...
Kondisi :
Lakukan Pengecekan apakah kata tersebut termasuk Palindrome 

Output :
Kata ..... Tidak Termasuk/ Termasuk Palindrome 

3.
(Gunakan hanya Fungsi Numerik-Aritmatik)
+ - * / % // 
Input : Masukkan 4 digit angka : 5493
Output nya :
9354

4.
(Gunakan Hanya Fungsi-Metode Numerik-Aritmatik)
Input :
Masukkan 2 digit angka : 63
Masukkan 2 digit angka kedua : 87 

Output : 6387

Kondisi untuk Soal 3-4 :
Tidak Menerima Inputan String
Tidak menerima inputan Negatif 
Tidak Menerima Inputan Desimal 
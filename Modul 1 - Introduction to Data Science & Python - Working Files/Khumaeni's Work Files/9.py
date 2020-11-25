'''
### Data Structured
List_A = [1,2,3] ==> list()
Tuple_A = (1,2,3) ==> tuple()
Set_A = {1,2,3} ==> set()


### Dictionary - Asosiasi - Mapping
Kamus 
Kata : Definisi
Keyword : Definition 
Key : Value 
- Yg memisahkan antara Key dan Value adalah tanda titik dua (:)
- Key + Value ==> Item ==> Gabungan antara Key dan Value 
- Yg memisahkan antar Item adalah tanda koma (,)

Key = Umumnya berupa String atau Integer
Value => Bisa berbentuk tipe data apapun (String, Integer, Float, Boolean, List, Tuple, Set, Dictionary)

List ==> Menggunakan Index (Integer - Numerik)
Dict ==> Menggunakan Key - "Nama"

Dict_A = {}
Dict_B = dict()

Data = {key : value,
        key2 : value2,
        key3 : value3,
        key4 : value4}
'''
nilai = {"andi" : 80,
        "andre" : 75,
        "beni" : 85,
        "bondan" : 90,
        "joko" : 87,
        1 : ["Rendi", 80]}

## Read - Baca-Akses Data 
# Basic Syntax :
# NamaDictionary[Keyword]

### Akses Value Menggunakan Key
# print(nilai['andi'])
# print(nilai['bondan'])
# print(nilai['joko'])
# print(nilai[1]) ### 1 disini Bukan Index, 1 merupakan Key

# print(nilai) ## Mencetak Dictionary
# print(list(nilai.keys())) ## Mencetak Keys dari Dictionary,
# Kemudian mengubahnya menjadi List
# print(nilai.values()) ## Mencetak Values dari Dictionary
# print('='*100)
# print(nilai.items()) ## Mencetak Items dari Dictionary

# print(nilai["cici"])  ## Akan keluar Error karena Tidak ada Key - Cici
'''
## Alternatif Lain untuk Akses Dictionary
print(nilai.get("andi")) ## Jika datanya ada, fungsi sama persis 
# seperti akses data langsung menggunakan Key

print(nilai.get("Cici", "Data Tidak Ada")) ## Jika data tidak ada, Tidak memunculkan Error

print(nilai.get("bondan", "Data Tidak Ada"))
'''
### Create - Menambah Data
# Basic Syntax :
# namaDict[Keyword] = Values
# Keyword merupakan Keyword baru yg belum ada di dalam Dict Sebelumnya
# print(nilai.get("joni", "Data Tidak Ada"))
nilai["joni"] = 84

# print(nilai['joni'])

### Update - Mengubah Data
'''
Basic Syntax :
namaDict[Keyword] = Values 
- Keyword => Menggunakan Keyword Lama, sebelumnya sudah ada 
- Key Lama yg Value nya akan diupdate
- Value => Value Baru untuk Mengupdate Value Lama 
'''
# print(nilai)
# Update nilai joni menjadi 95
nilai['joni'] = 95 ## Masukkan Key yg akan diupdate Value nya dan Value Baru
# print(nilai)

nilai.update({"joni" : 90})

nilai.update({"desi" : 85})
# Jika menggunakan fungsi .update
#langsung masukkan format Items
# Jika menggunakan Keys yg sudah ada, akan mengubah Value dari keys tsb
# Jika menggunakan keys baru, akan menambah Item baru ke dalam dict
# print(nilai['joni'])
# print(nilai['desi'])

A = nilai["joni"]

nilai["jack"] = A
'''
print(nilai)
print(nilai['jack'])
'''
for i in nilai.keys():
        if i == 'jack' or i == 'joni':
                nilai[i] = 95

# print(nilai)

### Delete - Hapus Data ==> Akan Menghapus 1 Items
# Basic Syntax:
# nilai.pop(Keys)

nilai.pop('joni')

# print(nilai.get('joni', 'Data Tidak Ada'))
# print(nilai)

nilai.pop(1)

DaftarNilai = list(nilai.values())

# print(DaftarNilai)

DaftarSiswa = list(nilai.keys())
# print(DaftarSiswa)

NilaiSiswa = list(nilai.items())
# print(NilaiSiswa)

# Nama = input("Masukkan Nama Siswa : ")
# Nilai = nilai.get(Nama, "Siswa yang anda cari Tidak Ada")

# print(f"Nilai dari : {Nama} adalah : {Nilai}")

Nilai_Baru = {}

A = len(DaftarSiswa)

for i in range(A):
        Nilai_Baru[DaftarSiswa[i]] = DaftarNilai[i]

# print(Nilai_Baru)

### Kamus Hari
Hari = {"senin" : "monday",
        "selasa": "tuesday",
        "rabu": "wednesday",
        "kamis": "thursday",
        "jum'at":"friday",
        "sabtu" : "saturday",
        "minggu" : "sunday"
}
# hari = ["senin", "selasa", dst]
# Hari_inggris = {'monday' : 'senin'}

# print(list(Hari.items()))

# Item_Hari = list(Hari.items())

# for i, j in Item_Hari:
#         print(i)
#         print(j)

# hari = input("Masukkan Nama Hari : ")

# eng = Hari[hari]
# print(f"Hari {hari} dalam bahasa inggris adalah {eng}")

### Latihan
'''
Auto - Translator

Input :
Masukkan Nama Hari : 

Kondisi :
- Tidak Case Sensitif 
- Tidak menerima inputan bukan hari, integer, float, dll

Keluar Notif : Nama Hari yg anda masukkan salah 

Output :
Tergantung Inputan 
- Jika Inputan Hari dalam bahasa Indo 
==> (f"Hari {hari} dalam bahasa inggris adalah {eng}")

- Jika Inputan Hari dalam bahasa Inggris 
==> (f"{hari} in bahasa is {indo}")
'''

member = {
        "name" : "Andre",
        "age" : 25,
        "is_married" : False,
        "height" : 170.5,
        "weight" : 59.5,
        "job" : "Data Analyst",
        "cars" : ["Alphard", "Xpander", "Jazz"],
        "address" : {
                "street" : "East Independence",
                "RT" : 6,
                "RW" : 4,
                "No" : 20,
                "City" : ["West Jakarta", "East Jakarta", "South Jakarta"],
                "Zipcode" : 58647,
                "geo" : {
                        "lat" : 58.69,
                        "lng" : [89.25, 63.58, 60.80, [25.2, 98.7]]
                }
        }
}

## Kita akan akses 98.7

print(member["name"])
print(member['height'])
print(member['is_married'])
print(member['cars'][1])

print(member['address']['street'])
print(member['address']['No'])

print(member['address']['City'][1])

print(member['address']['geo']['lat'])
print(member['address']['geo']['lng'][2])

print(member['address']['geo']['lng'][3])
print(member['address']['geo']['lng'][3][1])

member['cars'][1] = "Yaris"
print(member['cars'])
member['address']['City'][2] = "North jakarta"

print(member['address']['City'])

member['address']['geo']['lng'][3][1] = 1800

print(member['address']['geo']['lng'])

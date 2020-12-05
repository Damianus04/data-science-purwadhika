'''
Data Structure  ==> Data yg berisi beberapa data primitif / data structure lain

--- Iterable Data

Tipe Data Primitif ==> Integer, Float, String, Boolean 

### List, Tuple, Set, Dictionary 

List
Menggunakan => [ ]

List_A = [data1, data2, data3, dst]
## Fungsi untuk mengubah Tipe data structure
list(data)  ### Mengubah Data menjadi List
'''

# sentences = 'hari ini adalah hari kamis'
# print(sentences.split(" "))  ### String yg di SPLIT akan menghasilkan LIST

hari = ['senin', 'selasa', 'rabu', 'kamis', "jum'at", 'sabtu', 'minggu']

data_list = ['senin', 25, True, 5.5, ['andi', 'rendi', ['HR', 'Finance']]]
'''
A = data_list[4][2][1]
# B = A[1]
print(A)
'''

# Cara Akses / Membaca Element dalam List (satu elemen)
# Menggunakan Indexing ==> Urutan angka, dimulai dari NOL, berupa angka INTEGER, Maksimal jumlah element terakhir-1
# Syntax :
# NamaList[noIndex]
'''
print(hari[0])
print(hari[3])
print(hari[2])
print(hari[-1])


## Cek Jumlah Data/Element dalam List
# Syntax :
# len(NamaList)

print(len(hari))

print(hari)  ### Melihat Keseluruhan Isi List

## Mengakses Element List Menggunakan Looping
for i in hari:
    print(i)

### Untuk Mengetahui Index suatu Element dalam List
Syntax :
NamaList.index(Element)

print(hari.index('rabu'))
print(hari[2])
print(hari.index('minggu'))
print(hari.index('kamis'))
print(hari[4])
'''
### Slicing
## Akses Beberapa Element List sekaligus
# NamaList[START : END : STEP]
# STEP => Ketika tidak ditentukan (Bernilai Default), berarti menggunakan Penjumlahan 1 (Increment)
# STEP => Default +1


# [START : END]
# Berlaku
# START : Inclusive => Index yg ditentukan akan di akses
# END : Exclusive => Index yg akan diakses END - 1 (Increment), END + 1 (Decrement)

# [Index]  => Akses Index tersebut (satu Element)

# print(hari.index('kamis'))
# print(hari.index('selasa'))

A = hari[ 3 : : -1]
# print(A)
'''
print(hari[1:3]) ## akan mengakses Index 1 sampai dengan index 2 (End - 1)
print(hari[2:]) ## akan mengakses index 2 sampai Index terakhir (Paling akhir)
print(hari[:4]) ## akan mengakses index paling awal sampai index ke 3 (End-1)
print(hari[:]) ## akan mengakses keseluruhan elemen, dg STEP +1 (Increment)
print(hari[::-1]) ## akan mengakses keseluruhan elemen, dg STEP -1 (Decrement)
'''

### Menambahkan Element (Data Baru) ke dalam List
## Fungsi Append
'''
Syntax :
NamaList.append(data)

## Fungsi Extend
Syntax :
NamaList.extend(data)
'''

nama = ['andi', 'beni', 'doni']
nilai = [89, 90, 78]


# nama.append('fitri')
# nama.extend('gina')
# nama.append(nilai)  ### Output ['andi', 'beni', 'doni', [89, 90, 78]]
# Ketika menambahkan data menggunakan append ==> Data akan dianggap sebagai Data Tunggal
nama.extend(nilai) ### Output ['andi', 'beni', 'doni', 89, 90, 78]
## Menambahkan data menggunakan extend ==> Element data yg akan ditambahkan
# print(nama)

### Menambahkan Data di Index Tertentu
# Secara Default, Ketika kita menambahkan Data ke dalam List, data akan berada di Index terakhir
hari.append('sunday')
# print(hari)

### Fungsi Insert
# Syntax :
# NamaList.Insert(Index, Datanya)
hari.insert(1, 'monday') ### Index 1 akan berubah sesuai input data, data lain dibelakang data baru akan Mundur Indexingnya
# print(hari)

hari.insert(4, 'wednesday')
# print(hari)

# hari1 = print()

# print(hari.insert(1, nilai))
# print(print(5)) ### Hasilnya akan sama seperti append
# print(hari)
### Mengubah / Mengupdate Data / Element dalam List
'''
Syntax :
NamaList[index] --- Data yg akan diubah/diupdate--- = Data Baru 
'''
# hari = 'selasa'
# hari = 'sela4sa'
## update monday menjadi senin2
# print(hari.index('monday'))
hari[1] = 'senin2'

# print(hari)
# paragraf.replace('data lama', 'data baru')
data = ['andi', 'beni', 'doni', [89, 90, 78]]

# print(data.index([89, 90, 78]))

# print(data[3].index(90))

data[3].insert(1, 95)
# print(data)


### Menghapus Elemen/Data dalam List
### Menghapus berdasarkan Data
# Remove
# Syntax :
# NamaList.remove(data) # data yg akan dihapus
# print(hari)
# hari.remove('sunday')
# print(hari)


### Menghapus berdasarkan Index
# pop
# Syntax :
# NamaList.pop(Index) ### Index data yg akan dihapus

# NamaList.pop() ## Jika Index dikosongkan, Data yg akan dihapus adalah Index terakhir
hari.pop() #menghapus Index terakhir
# print(hari)

hari.pop(1) #menghapus Index 1 (senin2)
# print(hari)

# ========================================================================

angka = [35, 71, 5, 100, 250, 90, 45, 5]

print(max(angka))
print(min(angka))
print(sum(angka))
print(angka.count(5))
angka.sort() ## Mengurutkan data dari yg terkecil ke yg terbesar (Update data awal)
print(angka)
angka.sort(reverse=True) ### Mengurutkan data yg terbesar ke yg terkecil
print(angka)



######################### Team Assignment 
- Kelompok 2-3 orang
Mini Aplikasi 
CRUD - Create - Read - Update - Delete 

Aplikasi Mini Untuk Data Barang / Elektronik / Buah / ATK dll

--- Apps awal di Run - Akan meminta Login (Password) 
-- Batas 4X
- Jika salah Password sampai 4X akan keluar aplikasi 

Jika Password Benar :
Akan Keluar Menu 

---Menu ----
1. Cetak Isi Daftar Barang (Read)
2. Menambahkan Data Barang (Create)
3. Mengubah Data Barang (Update)
4. Menghapus Data Barang (Delete)
5. Exit (Keluar Apps)

--- Kondisi (T&C)
1. Read (Cetak Data)   
- Jika tidak ada Data, akan keluar Notif : Daftar Barang Masih Kosong 
- Jika ada Data, Akan menampilkan seluruh data barang 

2. Create (Tambah Data)  
- Pengecekan jenis data, Jika salah format : Data yg anda masukkan salah 
- Pengecekan Duplikasi :
Jika data sudah ada sebelumnya,
Keluar notif :
Data sudah ada, Apakah tetap akan disimpan? (Y/N) 
Y : Keluar Notif = Data Tersimpan =====> Data akan disimpan 
N : Keluar Notif = Data Tidak tersimpan 
- Ketika data berhasil disimpan keluar notif : Data Berhasil di simpan  (Jika tidak ada duplikasi)

3. Update (Ubah Data) 
- Program akan meminta user memasukkan Data yg akan diupdate 
- Jika data yg diminta user tidak ada keluar notif : Data Barang Tidak Ada 
- Jika barang ada => Update Datanya ==> Jeruk -- Jeruk Bali 
- Keluar Notif : Data Terupdate/ Data berhasil diubah 

4. Delete (Hapus Data)  
- Program akan meminta user memasukkan Data yg akan dihapus 
- Jika data yg diminta user tidak ada keluar notif : Data Barang Tidak Ada
- Jika barang ADA ==> Hapus Seluruh data yg sesuai dg inputan user 

5. Exit 
- Selama User belum memilih opsi ini, Menu akan terus ditampilkan 

Setelah melakukan proses CRUD (akan keluar mini menu yg memiliki 2 opsi)
1. Kembali Ke Menu Utama 
2. Ke Menu awal (yg diakses)

Kirim Email : khumaeni@purwadhika.com 
Deadline Selasa sebelum kelas 
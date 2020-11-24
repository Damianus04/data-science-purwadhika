## SET
'''
- Unordered List 
- Unique
- Non Indexing 
- Tidak bisa mengandung Data List, Tetapi bisa mengandung Tuple karena Tuple bersifat Immutable
- Sama dengan HIMPUNAN pada Math

set_A = {data}
set_B = set()
'''
A = {2,5,89,30,21,25,145,12,(25,2,5),89,30,21,25,145,12,25,2,5,89,30,21,25,145,12,25,2,5,89,30,21,25,145,12,25}

# print(A)

### Menambahkan Data - Create
# Update ==> Sama konsepnya dengan Extend pada List
A.update('Caca')  #### Mirip dengan fungsi Extend pada List => Menambahkan Setiap Elemen
A.update(['Geri', 'Andre'])
A.update(['Caca'])
A.update([968]) ### Fungsi Update, Tidak bisa langsung Menambahkan Data Integer/Float
# print(A)

# Add ==> Sama konsepnya dengan Append pada List
A.add('Desi') ### Mirip dengan fungsi Append pada List
A.add(96)
A.add(('Desi'))
# print(A)

# print(A[2])

### Hapus Data - Delete
## Remove
A.remove('c')
# A.remove(100) ## Akan mengeluarkan Error, jika data tidak ada
A.discard(100)  ## Tidak akan keluar Error, meskipun data Tidak Ada
# print(A)

### Menghapus seluruh Elemen dalam SET
# A.clear()
# print(A)

### Menghapus Seluruh Elemen beserta SET
# del A
# print(A)

######## Operasi Himpunan Pada SET

X = {7, 8, 9, 10, 11}
Y = {7, 8, 15, 20, 25}

## Gabungan - Union ( Gabungan antara 2 atau lebih Himpunan/SET)
z = X.union(Y) ## Menggunakan fungsi union

z1 = Y.union(X)
print(z)
print(z1)

print(X | Y)  ### Menggunakan Simbol Union | 
print(Y | X)

## Irisan - Intersection ==> Menampilkan data yg beririsan

v = X.intersection(Y) ## Menggunakan Fungsi Intersection
v2 = Y.intersection(X)

print(v)
print(v2)

print(X & Y) ## Menggunakan Simbol irisan-intersection ( & )
print(Y & X)

### Selisih - Difference

W = X.difference(Y) ## Menggunakan fungsi difference
W2 = Y.difference(X)

print(W)
print(W2)

print(X - Y) ## Menggunakan Simbol -
print(Y - X)

### Beda Setangkup - Symmetric Difference

R = X.symmetric_difference(Y) ## Menggunakan Fungsi Symmetric Difference
R2 = Y.symmetric_difference(X)
print(R)
print(R2)

print(X ^ Y) ## Menggunakan simbol ^
print(Y ^ X)

## Latihan
A = Himpunan Bilangan Genap dari 1 - 20
B = Himpunan Bilangan Ganjil dari 1 - 20
C = Himpunan bilangan Negatif lebih besar dari -20
D = Himpunan Bilangan Prima dari 1 - 20
E = Himpunan Bilangan Komposit dari 1 - 20
Bilangan Komposit = Bukan Bilangan Prima 

u = Union
n = Irisan

a. A u B u C u D u E
b. (A n B) u (D n E)
c. (A u B) n (D u E)
d. (A u B) - (D u E)
e. (A u B u C) - (A n E)

## Membuat data isi himpunan nya menggunakan Fungsi
A = {2, 4, 6, 8, 10, 12, ...}
a = 50, 70, 90

a = b = c = 45
# a, b, c = 45  ==> Akan menghasilkan error, karena jumlah var tidak sama
nama = "Joni\n Andre"
NAMA = "Joni Andre"
index = a * b

print(len(nama))
print(len(NAMA))
# print(nama[2:3])
# # untuk slicing nilai END minimal adalah START + 1 agar bisa running dg baik 

# print(nama[1:10])
# # print(nama[10])
# print(nama[9])
# print(nama[-10])

# print(nama[-11:10])
# print(nama[-30:10])
# print(nama[-25:15])

# print(nama[1:15])
# print(nama[15])
### Slicing tidak akan memunculkan Error, meskipun nilai index melebihi index maksimum,
# sedangkan Indexing akan memunculkan Error = Index out of range

# print(nama[:6])  ### Akses index paling awal sampai Index 5 (6-1)

# print(nama[3:])  ### Akses index dari index 3 sampai index paling akhir

# print(nama[:])  ##Akses index paling awal hingga index paling akhir

# print(nama[ ]) ### Akses Indexing tidak bisa menggunakan metode angka kosong

# print(nama[::-1])

# a = 5.8
# print(a)

# print(int(5.8))

# print(int('5.8'))
# b = 'empat lima'
# print(float(b))
# print(int(b))
# print(b.isdecimal())
# c = '0'
# print(c.isdigit())
# print(int(c))

# berat = 'empat puluh lima'
# if berat.isdigit() == False:


###
# Jika akan mengubah tipe data String menjadi Integer (Tidak menerima Pembulatan),
# Oleh karena itu, String yg dapat diubah menjadi Nilai Integer adalah Angka Bulat dari Negatif, Nol dan Positif

# val = int(input("Masukkan Value : "))
# if val.isdigit() == False:
#     print("Angka yang anda masukkan salah")
# print(val)

angka = 80
# print(len(angka))
# print("Angka yang anda \n masukkan salah")
# \n ==> New Line ==> Escape Character
# 8.4
# 8 7
# tiga puluh 

print(round(2.23452, 3))
print(round(2.23352, 3))

print(round(2.5))
print(round(3.5))
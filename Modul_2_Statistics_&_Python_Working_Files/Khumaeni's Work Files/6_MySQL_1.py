MySQL

Salah satu dari DBMS yg berbasis Relasi
Big Data - -> 3v
Volume
Variety
Velocity

RDBMS == > Relational Database Management System
Contoh RDBMS:
- MySQL, Oracle, Postgres, Ms. Access, Ms. SQL Server

Bahasa yg digunakan Secara de facto == > SQL(Structured Query Language)

DDL = > Data Definition Language == > Memanipulasi Struktur Database
DML = > Data Manipulation Language == > Memanipulasi struktur Data

MongoDB = > Camel Case
SQL = > Snake Case

MongoDB == > User akses terletak di masing-masing DB
MySQL == > User akses terletak di server

CRUD = > Create Read Update Delete

root == > Akses paling tinggi == > SuperAdmin

Kita dapat membuat user dg privilege yg sama dg root


# Bekerja dg SQL
- Server MySQL Berjalan secara auto run **
- Create User
- Login ke dalam server - sistem
- Create Database
- Use Database
- Create Table == > Membuat Tabel sekaligus Struktur Tabel(Nama Kolom dan Tipe data untuk kolom tersebut)
- Insert Data sesuai dg Struktur Tabel
- Bisa melakukan DML

Data == > Tuple(Rows), Field(Columns)

== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
Tipe Data di SQL
- Numerik
- String
- Date
- Text


== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
NUMERIK:
- Integer
- Fixed Point
- Floating Point


Integer: Bilangan Bulat(Bukan Pecahan/Desimal)
- TinyInt == > -128 s/d 127
- SmallInt == > -32.768 s/d 32.767
- MediumInt == > -8.3juta s/d 8.3juta
- INT == > -2.1 Milyar s/d 2.1 milyar
- BigInt = > -9.2 quadrillion s/d 9.2 quadrillion


Paket Internet == > ISP == > 200GB Per Bulan
rata-rata penggunaan 15GB Per bulan

ternyata rata-rata penggunaan 5GB Per bulan
Langganan 10GB
usia: 25, 30, 24
usia: "-2.75"
usia: "tiga puluh"

== == == == == == == == == == == == == == == == == == == == == == == == == ==
Jenis tipe data Fixed Point == > Bilangan Pecahan/Desimal,
yg angka dibelakang komanya, sudah diatur dari awal.
Define dg 2 digit angka
- Digit pertama: Menunjukan jumlah seluruh digit angka
- Digit Kedua: Menunjukkan Jumlah koma dibelakang angka
DECIMAL(4, 2) == > Total digit angka ada 4, Total digit angka dibelakang koma ada 2
-99.99 s/d 99.99

DECIMAL(4, 1) == > -999.9 s/d 999.9
DECIMAL(3, 2) == > -9.99 s/d 9.99
DECIMAL(3, 1) == > -99.9 s/d 99.9

Angka Pertama Maksimal 65
Angka Kedua Maksimal 30
DECIMAL(65, 30)

== == == == == == == == == == == == ==
FLOATING POINT == > Bilangan Desimal/Pecahan Tetapi angka dibelakang koma maupun total digit, bisa berbeda setiap baris
- Float
- Double == > 2X float == > Size 2X lipat

== == == == == == == == == == == == ==
String
- Char == > 255 karakter
- Varchar == > 65.535 karakter

== > Binary & VarBinary == > Metode penyimpanan char dengan Biner

== == == == == == == == == == == == ==
Text
TinyText == > 255 char
Text == > 65.535 char
MediumText == > 16.7 jutaan char
LongText == > 4.2 milyaran


== == == == == == == == == == == == ==
Date
Date == > Tanggal
DATETIME == > Tanggal dan Jam
TIMESTAMP == > tanggal dan jam ketika data diinput
TIme == > Jam
Year(2) == > Format tahun 2 digit == > 94, 45
YEar(4) == > Format tahun 4 digit == > 1994, 1945


== == == == == == == == == == == == ==
ENUM == > Mirip dengan pilihan radio button / combo box
User hanya dapat memilih salah satu dari pilihan data yang sudah di define sebelumnya

Contoh: Gender
- Male
- Female

Max == > 65.535 pilihan


== == == == == == == == == == == == ==
Tipe data SET == > Mirip dengan Checkbox

Mirip dengan ENUM, tetapi user dapat memilih lebih dari 1 pilihan yang tersedia

Contoh: Hobi

max == > 64 Pilihan


== == == == == == == == == == == == ==
Atribut Tipe Data
- Auto_Increment == > Penambahan otomatis 1 angka == > 1 kolom
- Default == > NULL(Kosong)
Nama Default(Anonim)

Jika user tidak - mengosongkan kolom Nama, maka nama akan tersimpan


Range tipe data akan lebih panjang

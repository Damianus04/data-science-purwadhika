# Mengkoneksikan MySQL dengan Python
'''
Package yg akan digunakan
mysql-connector-python

- pyMysql
- SQLLite
- SQLAlchemy

py -m pip install mysql-connector-python
pip3 install mysql-connector-python
pip install mysql-connector-python

'''

import mysql.connector

# print('Import Success')

### Server --- Client

# Server

# - Definisikan Server
# - Definisikan User Akses
# - Definisikan Database

myDB = {
    'user': 'damianus',
    'password': '12345',
    'host': 'localhost',
    'database': 'sales'
}

# CLient

# Definisikan Client
conn = mysql.connector.connect(**myDB)

# print('Connection Success')

C = conn.cursor()  # digunakan untuk mengeksekusi query SQL

# Describe Tabel

query = 'DESCRIBE employee'

C.execute(query)

for i in C:
    print(i[0], i[1])


# Membuat Tabel Baru
'''
query = """ CREATE TABLE Department 
(Dept_ID char(10), Dept_Name char(30))
"""

C.execute(query)
print('Table Created')
'''

# Masukkan Data ke dalam Tabel
'''
query = "INSERT INTO Department VALUES ('D01', 'Finance')"

C.execute(query)

conn.commit() ### Ketika melakukan Data Manipulation (Create, Update, Delete), Harus ditambahkan Commit
print('Data Submitted')
'''

# Alternative untuk memasukan data
'''
sql = 'INSERT INTO Department VALUES (%s, %s)'
val = ("D02", "Accounting")

C.execute(sql, val)
conn.commit()

print('Data Submitted')


sql = "INSERT INTO employee (nama, kota, gaji) VALUES (%s, %s, %s)"
val = ("Bayu", "Malang", "26000000")
C.execute(sql, val)

conn.commit()

print('Data Submitted')
'''

# Memasukkan Banyak Data
'''
sql = "INSERT INTO Department VALUES (%s, %s)"
val = [
    ("A01", "HR"),
    ("C02", "Marketing"),
    ("E04", "Data")
]

C.executemany(sql, val)
conn.commit()

print("data submitted")
'''

# Mengakses Data
# Alt 1
'''
query = "SELECT * from Department"

C.execute(query)

for i in C:
    print(i[0], i[1])
'''
# Alt 2
'''
query = "SELECT * FROM Department"
C.execute(query)

hasil = C.fetchall()

for i in hasil:
    print(i[0], i[1])
'''
# Variasi Select
'''
query = "SELECT * FROM DEPARTMENT LIMIT 3"

C.execute(query)

for i in C:
    print(i)
'''

# UPDATE DATA
'''
query = "UPDATE Employee Set usia='24' WHERE nama='Bayu'"
C.execute(query)

conn.commit()
print('Data Updated')
'''
# HAPUS DATA
'''query = "DELETE FROM Employee WHERE Nama = 'Bayu'"
C.execute(query)

conn.commit()
print('Data Deleted')'''

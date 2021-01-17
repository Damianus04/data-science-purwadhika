# import library
import mysql.connector
# print('success')

# Define Server, User Access, Database
myDB = {
    'user': 'damianus',
    'password': '12345',
    'host': 'localhost',
    'database': 'sales'
}

# Define Client
connection = mysql.connector.connect(**myDB)
C = connection.cursor()  # used for executing SQL query

##############################################################
# SQL Query

# Showing Databases
'''query = 'SHOW DATABASES'
C.execute(query)
for i in C:
    print(i)

    # ('dbdamianus',)
    # ('information_schema',)
    # ('mysql',)
    # ('performance_schema',)
    # ('sales',)
    # ('sys',)
    # ('toko',)'''

# Describe Table
'''query = 'DESCRIBE employee'
C.execute(query)
for i in C:
    print(i[0], i[1])

    # employeeID b'mediumint'
    # name b'char(50)'
    # gender b"enum('Male','Female')"
    # salary b'int'
    # city b'varchar(50)'
    # age_range b'tinyint'
    # time_created b'timestamp'
'''

# Create New Table
'''query = """CREATE TABLE department
(dept_id char(10),
dept_name char(30))"""
C.execute(query)
connection.commit()'''

# Insert New Data - Alt 1
'''query = """INSERT INTO department VALUES
('D01', 'Finance'),
('D02', 'Economy')"""
C.execute(query)
connection.commit()'''

# Insert New Data - Alt 2
'''query = "INSERT INTO department VALUES (%s, %s)"
value = [
    ("A01", "HR"),
    ("C02", "Marketing"),
    ("E04", "Data")
]
# C.execute(query, value) # -> execute single data
C.executemany(query, value)  # -> execute many data
connection.commit()'''

# Accessing Data - Alt 1
'''query = 'SELECT * FROM department'
C.execute(query)
for i in C:
    print(i[0])

    # D02
    # D01
    # A01
    # C02
    # E04'''

# Accessing Data - Alt 2
'''query = "SELECT * FROM department"
C.execute(query)
result = C.fetchall()

for i in result:
    print(i[0], i[1])

    # D02 Economy
    # D01 Finance
    # A01 HR
    # C02 Marketing
    # E04 Data'''

# Update Data
'''query = """UPDATE employee SET age_range='24'
WHERE name='Cindy'"""
C.execute(query)
connection.commit()'''

# Delete Data
'''query = """DELETE FROM employee
WHERE name='Cindy' AND city='Jakarta'"""
C.execute(query)
connection.commit()'''

from flask import request, jsonify, Flask
from mysql.connector import connect, cursor

app = Flask(__name__)

# connection to mysql
myDB = {
    'user': 'damianus',
    'password': '12345',
    'host': 'localhost',
    'database': 'sales'
}
connection = connect(**myDB)
# cursor = connection.cursor()

# Route to API
# get dan post method
@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'GET':
        # query untuk digunakan
        sql_query = 'SELECT * FROM employee'

        # membuka koneksi ke db
        cursor = connection.cursor()

        # eksekusi perintah sql
        cursor.execute(sql_query)

        # fetch all data from query result
        query_result = cursor.fetchall()

        # return query_result data to API
        return jsonify(query_result)

    elif request.method == 'POST':
        # post untuk melakukan post data/memasukkan data ke db
        # data yang dikirim saat request ada di requests.form
        # data tersebut diubah menjadi dictionary
        form = dict(request.form)

        # menyimpan data ke variable
        name = form['name']
        gender = form['gender']
        salary = form['salary']

        # jika ingin mengubah menjadi boolean
        # married = bool(form['married'])

        # membuat query untuk menyimpan data di atas
        sql_query = """INSERT INTO employee
                        (name, gender, salary)
                        VALUES
                        (%s, %s, %s)"""

        # data yang akan disimpan dimasukkan ke variabel
        data = (name, gender, salary)

        # membuka koneksi ke mysql
        cursor = connection.cursor()

        # eksekusi perintah
        cursor.execute(sql_query, data)

        # commit input data ke DB agar tersimpan lalu close supaya
        # tidak banyak koneksi terbuka
        connection.commit()
        cursor.close()

        # mengubah data dictionary menjadi json untuk dikirim balik
        return jsonify({'message': f'insert succes, name: {name}'})

# Route PATCH, DELETE
@app.route('/employee/<id>', methods=['PATCH', 'DELETE'])
def employee_id(id):
    if request.method == 'PATCH':
        # ambil data dari form yang masuk
        form = dict(request.form)

        # menyimpan data ke variable
        name = form['name']
        gender = form['gender']
        salary = form['salary']

        # jika ingin mengubah menjadi boolean
        # married = bool(form['married'])

        # membuat query untuk mengubah data berdasarkan employee id
        # menggunakan kutip 3 agar bisa newline

        sql_query = f"""UPDATE employee SET
                        name ='{name}',
                        gender = '{gender}',
                        salary = '{salary}'
                        WHERE employeeID={id}"""

        # membuka koneksi ke mysql
        cursor = connection.cursor()

        # eksekusi perintah
        cursor.execute(sql_query)

        # commit input data ke DB agar tersimpan lalu close supaya
        # tidak banyak koneksi terbuka
        connection.commit()
        cursor.close()

        # mengubah data dictionary menjadi json untuk dikirim balik
        return jsonify({'message': f'update succes', 'user_id': id})

    elif request.method == 'DELETE':

        sql_query = f'DELETE FROM employee WHERE employeeID = {id}'
        cursor = connection.cursor()
        cursor.execute(sql_query)

        connection.commit()
        cursor.close()

        return jsonify({'message': 'Delete success', 'user_id': id})

# check connection
# query = 'SHOW DATABASES'
# cursor.execute(query)
# for i in cursor:
#     print(i)


# menjalankan app jika script dipanggil
if __name__ == "__main__":
    app.run(debug=True)


# Tugas
# - Buat Database baru mengenai jabatan pegawai

# Tabelnya :
# | username | jabatan | gaji | tingkat |

# - Buat rute API jabatan untuk menambah dan mengupdate
# - pastikan data pegawai (username) tersedia di tabel employee
# - buatlah rute get pada sebuah id


# ujian
# mysql
# eda
# db
# dashboard

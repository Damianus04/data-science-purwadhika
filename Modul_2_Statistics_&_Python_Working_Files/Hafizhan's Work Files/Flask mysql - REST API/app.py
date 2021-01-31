# install note : pip install mysql-connector-python flask
# Memanggil flask sabagai fungsi untuk 
# membuat web app
from flask import request, jsonify, Flask
from mysql.connector import connect

# Memanggil flask sebagai aplikasi 
# untuk kita panggil
app= Flask(__name__)

## Kita membuat koneksi ke MYSQL db
sqldb = connect( host= "localhost"             # host mysql saya
                , user= "root"                 # username mysql saya
                , password= ""                 # password mysql saya
                , database= "flask_mysql"      # database yg kita buat
                )

## buat cursor ke mysql
cursor = sqldb.cursor()

## Buat rute ke API
# Get dan Post Method
@app.route('/employee', methods=['GET', 'POST'])
def employee():

    if request.method == 'GET':
        # Membuat Query untuk digunakan
        sql_query = "SELECT * FROM employee"
        
        # Membuka koneksi ke db
        cursor = sqldb.cursor()

        # eksekusi perintah sql
        cursor.execute(sql_query)

        # fetch all data from query result
        query_result = cursor.fetchall()

        # return query_result data to API
        return jsonify(query_result)

    elif request.method=='POST':
        # post kita tugaskan untuk melakukan post data/ memasukan data ke db
        # data yang dikirim saat request ada di requests.form
        # data tersebut kita ubah menjadi dictionary
        form = dict(request.form)

        # menyimpan data ke variabel
        username = form['username']
        name = form['name']
        gender = form['gender']

        # data married diubah jadi true or false / 0 atau 1
        married = bool(form['married'])

        # membuat query untuk menyimpan data diatas
        sql_query = """ INSERT INTO employee 
                        (username, name, gender, married) 
                        VALUES 
                        (%s, %s, %s, %s) """ # untuk kolom yang disiapkan untuk di isi pada string

        # data yang akan disimpan dimasukan ke variabel
        data = (username, name, gender, married)

        # membuka koneksi ke mysql
        cursor = sqldb.cursor()
        # eksekusi perintah    
        cursor.execute(sql_query, data)
        
        sqldb.commit() # commit input data ke DB agar tersimpan
        cursor.close() # tutup koneksi ke db

        # mengubah data dictionary menjadi json untuk dikirim balik
        return jsonify({'message': f'insert success, username : {username}'})


##### Route PATCH , DELETE
@app.route('/employee/<id>', methods=['PATCH', 'DELETE','GET', 'POST'])
def employeeid(id):
    
    if request.method == 'GET':
        # get data from id
        return jsonify({'message': f'ini adalah GET untuk {id}'})

    # aturan ketika ada request patch
    if request.method == 'PATCH':
        # ambil data formulir dari requests yang masuk
        form = dict(request.form)
        
        # menyimpan data ke variabel
        username = form['username']
        name = form['name']
        gender = form['gender']
        married= form['married']

        # membuat query untuk mengubah data berdasarkan employee id
        # menggunakan kutip 3 agar bisa newline 
        # menggunakan f di awal untuk menyisipkan variabel di string
        sql_query = f""" UPDATE employee SET 
                        username='{username}'
                        , name='{name}'
                        , gender='{gender}'
                        , married='{married}' 
                        WHERE id={id} """

        # membuka koneksi ke mysql
        cursor = sqldb.cursor()
        # eksekusi perintah
        cursor.execute(sql_query)
        # commit input data ke DB agar tersimpan
        sqldb.commit()
        cursor.close()

        return jsonify({'message': 'Update success', 'user_id': id})


    elif request.method == 'DELETE':

        sql_query = f"DELETE FROM employee WHERE id = {id}"
        cursor = sqldb.cursor()
        cursor.execute(sql_query)

        sqldb.commit()
        cursor.close()

        return jsonify({'message': 'Delete success', 'user_id': id})

# akan menjalankan app jika script dipanggil
if __name__ == "__main__":
    app.run(debug=True)
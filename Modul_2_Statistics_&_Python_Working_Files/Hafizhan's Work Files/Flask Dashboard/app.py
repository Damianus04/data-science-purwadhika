
# Flask : library utama untuk membuat API
# render_template : agar dapat memberikan respon file html
# request : untuk membaca data yang diterima saat request datang
from flask import Flask, render_template, request

# import plotly adalah library untuk membuat plot
import plotly
import plotly.graph_objs as go

# import pandas sebagai pengolah data
import pandas as pd
import json

# maemangiil flask sebagai aplikasi
app = Flask(__name__)

## CATEGORY PLOT ##
# Read data pandas from tips.csv in static folder
tips = pd.read_csv('./static/tips.csv')


def category_plot(
        cat_plot='histplot',
        cat_x='sex',
        cat_y='total_bill',
        estimator='count',
        hue='smoker'):

    # Read data pandas from tips.csv in static folder
    tips = pd.read_csv('./static/tips.csv')

    # kategori plot akan ada 2 yaitu box dan hist
    if cat_plot == 'histplot':
        # siapkan variabel kosong untuk menyimpan konfigurasi
        data = []

        # generate config histogram dengan mengatur sumbu x dan sumbu y
        for val in tips[hue].unique():        # ambil data unique saja untuk ambil datanya
            hist = go.Histogram(                  # graph object tampilkan histogram dgn var x,y,histfunc, nama kategori
                # operasi dataframe tips['smoker']['sex']
                x=tips[tips[hue] == val][cat_x],
                y=tips[tips[hue] == val][cat_y],    # operasi dataframe
                histfunc=estimator,               # estimator
                name=val                          # nama sumbu x nya / kategorinya
            )
            # masukkan ke dalam array
            # append all hue data / gabungin all loop data
            data.append(hist)
        # tentukan title dari plot yang akan ditampilkan
        title = 'Histogram Plot'

    elif cat_plot == 'boxplot':
        data = []
        for val in tips[hue].unique():
            box = go.Box(
                x=tips[tips[hue] == val][cat_x],  # series
                y=tips[tips[hue] == val][cat_y],
                name=val
            )
            data.append(box)
        title = 'Box Plot'

    # menyiapkan config layout tempat plot akan ditampilkan
    # menentukan nama sumbu x dan sumbu y
    if cat_plot == 'histplot':
        layout = go.Layout(               # mirip plt.figure
            title=title,                  # judul plotnya
            xaxis=dict(title=cat_x),      # label x
            yaxis=dict(title='person'),   # label y
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode='group'
        )

    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            boxmode='group')        # boxmode group digunakan berfungsi
        # untuk mengelompokkan box berdasarkan hue

    # simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    # json.dumps akan mengenerate plot dan menyimpan hasilnya pada graphjson
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
def index():

    # memanggil fungsi category_plot
    plot = category_plot()

    # DROP DOWN MENU
    # kita lihat pada halaman dashboard terdapat menu dropdown
    # terdapat lima menu dropdown, sehingga kita mengirimkan kelima variable di bawah ini
    # kita mengirimnya dalam bentuk list agar mudah mengolahnya di halaman html menggunakan looping
    # ini adalah list of variable (input, tampilan txt di web)
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('sex', 'Sex'), ('smoker', 'Smoker'),
              ('day', 'Day'), ('time', 'Time')]
    list_y = [('total_bill', 'Bill'), ('tip', 'Tip'), ('size', 'Size')]
    list_est = [('count', 'Count'), ('avg', 'Average'),
                ('max', 'Max'), ('min', 'Min')]
    list_hue = [('sex', 'Sex'), ('smoker', 'Smoker'),
                ('day', 'Day'), ('time', 'Time')]

    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot='histplot',    # default plot yang tampil
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x='sex',

        # untuk sumbu Y tidak ada, nantinya menu dropdown Y akan di disable
        # karena pada histogram, sumbu Y akan menunjukkan kuantitas data

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator='count',
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue='smoker',
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot=list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x=list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y=list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator=list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue=list_hue

    )


# Bikin route index/ home page
# @app.route('/')
# def index():
#     return render_template('index.html')
# fungsi index kita jalankan (laukan render page)
# untuk file index.html

# jalankan fungsi ketika file py ini dipanggil
if __name__ == '__main__':
    app.run(debug=True)

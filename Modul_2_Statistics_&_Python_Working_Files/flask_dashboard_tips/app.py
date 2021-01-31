# Flask: library utama membuat API
# render_template: agar dapat memberikan respon file html
# request: untuk membaca data yang diterima saat request datang
from flask import Flask, render_template, request, url_for
from numpy.lib.histograms import histogram

# plotly: library untuk membuat plot
import plotly
import plotly.graph_objs as go
import pandas as pd
import json

# memanggil flask sebagai aplikasi
app = Flask(__name__)


# Read data pandas from tips.csv in static folder
tips = pd.read_csv('./data/tips.csv')


###################
# HIST & BOX PLOT #
###################
def category_plot(
        cat_plot='histplot',
        cat_x='sex',
        cat_y='total_bill',
        estimator='count',
        hue='smoker'):

    tips = pd.read_csv('./data/tips.csv')
    title = "Histogram Plot"
    data = []

    # karegori plot akan ada 2, yaitu box dan hist
    if cat_plot == 'histplot':
        data = []

        # generate config histogram dengan mengatur sumbu x dan y
        for val in tips[hue].unique():
            hist = go.Histogram(
                # operasi dataframe tips['smoker']
                x=tips[tips[hue] == val][cat_x],
                y=tips[tips[hue] == val][cat_y],  # operasi dataframe
                histfunc=estimator,               # estimator
                name=val                          # nama sumbu x/kategori
            )
            # masukkan dalam array
            data.append(hist)                   # append all hue data
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

    # menyiapkan config layout templat plot akan ditampilkan
    # menentukan nama sumbu x dan sumbu y
    if cat_plot == 'histplot':
        layout = go.Layout(             # mirip plt.figure
            title=title,                # judul plot
            xaxis=dict(title=cat_x),     # label x
            yaxis=dict(title='person'),  # label y
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode='group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode='group'
        )

    # simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    # json.dumps akan mengenerate plot dan menyimpan hasilnya pada graphjson
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
def index():

    plot = category_plot()

    # DROP DOWN MENU
    # kita lihat pada halaman dashboard terdapat menu dropdown terdapat lima menu dropdown, sehingga kita mengirimkan kelima variable di bawah ini
    # kita mengirimnya dalam bentuk list agar mudah mengolahnya di halaman html menggunakan looping
    # ini adalah list of variable (input, tampilant text di web)
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
        drop_hue=list_hue)


###################
# HIST & BOX PLOT ROUTE #
###################

@app.route('/cat_fn/<nav>')
def cat_fn(nav):    # Fungsi 'cat_fn'
    # saat kita klik menu yang mengarah ke 'cat_fn', maka akan mereset value ke default
    if nav == True:
        cat_plot = 'histplot'
        cat_x = 'sex'
        cat_y = 'total_bill'
        estimator = 'count'
        hue = 'smoker'
    else:
        cat_plot = request.args.get('cat_plot')
        cat_x = request.args.get('cat_x')
        cat_y = request.args.get('cat_y')
        estimator = request.args.get('estimator')
        hue = request.args.get('hue')

    # dari bloxplot ke histogram akan none
    if estimator == None:
        estimator = 'count'

    # saat estimator == 'count', dropdown menu sumbu Y menjadi disabled dan memberikan nilai none
    if cat_y == None:
        cat_y = 'total_bill'

    # Dropdown menu
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('sex', 'Sex'), ('smoker', 'Smoker'),
              ('day', 'Day'), ('time', 'Time')]
    list_y = [('total_bill', 'Bill'), ('tip', 'Tip'), ('size', 'Size')]
    list_est = [('count', 'Count'), ('avg', 'Average'),
                ('max', 'Max'), ('min', 'Min')]
    list_hue = [('sex', 'Sex'), ('smoker', 'Smoker'),
                ('day', 'Day'), ('time', 'Time')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
    return render_template(
        # file yang akan jadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot=cat_plot,    # default plot yang tampil
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x=cat_x,
        focus_y=cat_y,

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator=estimator,
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue=hue,
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

##############
#SCATTER PLOT#
##############


def scatter_plot(cat_x, cat_y, hue):

    data = []
    for val in tips[hue].unique():
        scatt = go.Scatter(
            x=tips[tips[hue] == val][cat_x],
            y=tips[tips[hue] == val][cat_y],
            mode='markers',
            name=val
        )
        data.append(scatt)

    layout = go.Layout(
        title='Scatter',
        title_x=0.5,
        xaxis=dict(title=cat_x),
        yaxis=dict(title=cat_y)
    )

    result = {'data': data, 'layout': layout}
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


##############
#SCATTER PLOT ROUTE#
##############

@app.route('/scatt_fn')
def scatt_fn():
    cat_x = request.args.get('cat_x')   # ambil isi form html
    cat_y = request.args.get('cat_y')   # ambil isi form html
    hue = request.args.get('hue')       # ambil isi form html

    # WAJIB! default value ketika scatter pertama kali dipanggil
    if cat_x == None and cat_y == None and hue == None:
        cat_x = 'total_bill'
        cat_y = 'tip'
        hue = 'sex'

    # Dropdown Menu
    list_x = [('total_bill', 'Bill'), ('tip', 'Tip'), ('size', 'Size')]
    list_y = [('total_bill', 'Bill'), ('tip', 'Tip'), ('size', 'Size')]
    list_hue = [('sex', 'Sex'), ('smoker', 'Smoker'),
                ('day', 'Daytime'), ('time', 'Time')]

    # kita panggil plot nya
    plot = scatter_plot(cat_x, cat_y, hue)

    # render template html
    return render_template(
        'scatter.html',
        plot=plot,
        focus_x=cat_x,
        focus_y=cat_y,
        focus_hue=hue,
        drop_x=list_x,
        drop_y=list_y,
        drop_hue=list_hue
    )


##########
#PIE PLOT#
##########
def pie_plot(hue='sex'):
    vcounts = tips[hue].value_counts()
    labels = []
    values = []
    for item in vcounts.iteritems():
        labels.append(item[0])
        values.append(item[1])

    data = [
        go.Pie(
            labels=labels,
            values=values
        )
    ]

    layout = go.Layout(title='Pie', title_x=0.48)
    result = {'data': data, 'layout': layout}
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

##############
#PIE PLOT ROUTE#
##############


@app.route('/pie_fn')
def pie_fn():
    hue = request.args.get('hue')
    if hue == None:
        hue = 'sex'
    list_hue = [('sex', 'Sex'), ('smoker', 'Smoker'),
                ('day', 'Day'), ('time', 'Time')]
    plot = pie_plot(hue)

    return render_template('pie.html', plot=plot, focus_hue=hue, drop_hue=list_hue)


# membuat Route
# @app.route('/')
# def index():
#     return render_template('index.html')
# fungsi index kita jalankan (lakukan render page) untuk file index.html
if __name__ == '__main__':
    app.run(debug=True)

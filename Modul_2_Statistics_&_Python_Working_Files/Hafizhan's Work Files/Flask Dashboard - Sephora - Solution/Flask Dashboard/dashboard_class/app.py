# Flask : library utama untuk membuat API
# render_template : agar dapat memberikan respon file html
# request : untuk membaca data yang diterima saat request datang
from flask import Flask, render_template, request

# plotly dan plotly.graph_objs : membuat plot
import plotly
import plotly.graph_objs as go

# pandas : untuk membaca csv dan men-generate dataframe
import pandas as pd
import json

# untuk membuat route
app = Flask(__name__)

###################
## CATEGORY (Barplot and Box) PLOT ##
###################

## IMPORT DATA USING pd.read_csv
sephora = pd.read_csv('./static/sephora.csv')
top5_brands = sephora['brand'].value_counts()[:5].index
sephora = sephora[sephora['brand'].isin(top5_brands)].reset_index(drop=True)


# membuat si fungsi plot nya
def category_plot(
    cat_plot = 'histplot',
    cat_x = 'brand', cat_y = 'price',
    estimator = 'count', hue = 'brand'):

    # jika menu yang dipilih adalah histogram
    if cat_plot == 'histplot':
        # siapkan list kosong untuk menampung konfigurasi hist
        data = []
        # generate config histogram dengan mengatur sumbu x dan sumbu y
        for val in sephora[hue].unique():
            hist = go.Histogram(
                x=sephora[sephora[hue]==val][cat_x],
                y=sephora[sephora[hue]==val][cat_y],
                histfunc=estimator,
                name=val
            )
            #masukkan ke dalam array
            data.append(hist)
        #tentukan title dari plot yang akan ditampilkan
        title='Histogram Sephora'

    elif cat_plot == 'boxplot':
        data = []

        for val in sephora[hue].unique():
            box = go.Box(
                x=sephora[sephora[hue] == val][cat_x], #series
                y=sephora[sephora[hue] == val][cat_y],
                name = val
            )
            data.append(box)
        title='Box'

    # menyiapkan config layout tempat plot akan ditampilkan
    # menentukan nama sumbu x dan sumbu y
    if cat_plot == 'histplot':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='# Orders'),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )

    #simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    #json.dumps akan mengenerate plot dan menyimpan hasilnya pada graphjson
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# akses halaman menuju route '/' untuk men-test
# apakah API sudah running atau belum
@app.route('/')
def index():
    return render_template('index.html')

# ada dua kondisi di mana kita akan melakukan request terhadap route ini
# pertama saat klik menu tab (Histogram & Box)
# kedua saat mengirim form (saat merubah salah satu dropdown) 
@app.route('/cat_fn/<nav>')
def cat_fn(nav):

    # saat klik menu navigasi
    # ini adalah default value ketika awal masuk route ini
    if nav == 'True':
        cat_plot = 'histplot'
        cat_x = 'category'
        cat_y = 'number_of_reviews'
        estimator = 'count'
        hue = 'category'
    
    # saat memilih value dari form
    else:
        cat_plot = request.args.get('cat_plot')
        cat_x = request.args.get('cat_x')
        cat_y = request.args.get('cat_y')
        estimator = request.args.get('estimator')
        hue = request.args.get('hue')

    # Dari boxplot ke histogram akan None
    if estimator == None:
        estimator = 'count'
    
    # Saat estimator == 'count', dropdown menu sumbu Y menjadi disabled dan memberikan nilai None
    if cat_y == None:
        cat_y = 'number_of_reviews'

    # Dropdown menu [('input variables string','Label that show in drpp down menu')]
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('brand', 'Brand'), ('category', 'Category'), ('price', 'Price'), ('love', 'Love')]
    list_y = [('price', 'Price'), ('love', 'Love'), ('number_of_reviews', 'Num Reviews')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('brand', 'Brand'), ('category','Category')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot=cat_plot,
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x=cat_x,
        focus_y=cat_y,

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator=estimator,
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue=hue,
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue
    )

##################
## SCATTER PLOT ##
##################

# scatter plot function
def scatter_plot(cat_x, cat_y, hue, brand):

    # call dataset
    sephora = pd.read_csv('./static/sephora.csv')

    # mapping brand
    if brand == "SEPHORA_COLLECTION":
        brand = "SEPHORA COLLECTION"
    elif brand == "TOM_FORD":
        brand = "TOM FORD"

    # if brand all
    if brand == 'all':
        x = sephora
        sephora = x[x['brand'].isin(top5_brands)]
    else:
        x = sephora
        sephora = x[x['brand']==brand]

    data = []
    for val in sephora[hue].unique():
        scatt = go.Scatter(
            x = sephora[sephora[hue] == val][cat_x],
            y = sephora[sephora[hue] == val][cat_y],
            mode = 'markers',
            name = val
        )
        data.append(scatt)

    layout = go.Layout(
        title= 'Scatter',
        title_x= 0.5,
        xaxis=dict(title=cat_x),
        yaxis=dict(title=cat_y)
    )

    result = {"data": data, "layout": layout}
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


## SCATTER PLOT Route ##
@app.route('/scatt_fn')
def scatt_fn():

    # mengambil nilai argumen dari API (saat awal akan None)
    cat_x = request.args.get('cat_x')  # ambil isi formulir dari html name: cat_x
    cat_y = request.args.get('cat_y')  # ambil isi formulir dari html name: cat_y
    hue = request.args.get('hue')    # ambil isi formulir dari html name: hue
    brand = request.args.get('brand')    # ambil isi formulir dari html name: hue

    # WAJIB! default value ketika scatter pertama kali dipanggil
    if cat_x == None and cat_y == None and hue == None:
        cat_x = 'number_of_reviews'
        cat_y = 'price'
        hue = 'brand'
        brand = 'all'

    # Dropdown menu list
    list_x = [('number_of_reviews', 'Num Reviews'), ('price', 'Price'), ('love', 'Love')]
    list_y = [('number_of_reviews', 'Num Reviews'), ('price', 'Price'), ('love', 'Love')]
    list_hue = [('brand', 'Brand')]
    list_brand = [('all', 'All') ,('SEPHORA_COLLECTION', 'Sephora'), ('CLINIQUE', 'Clinique')
                , ('tarte', 'Tarte'), ('TOM_FORD', 'Tom Ford'),  ('Dior', 'Dior')]

    # kita panggil si plot nya
    plot = scatter_plot(cat_x, cat_y, hue, brand)

    # render template html
    return render_template(
        'scatter.html',
        plot=plot,
        focus_x=cat_x,
        focus_y=cat_y,
        focus_hue=hue,
        focus_brand=brand,
        drop_x= list_x,
        drop_y= list_y,
        drop_hue= list_hue,
        drop_brand = list_brand
    )


##################
## LINE PLOT ##
##################

# line plot function
def line_plot(cat_x, cat_y, hue):

    # call dataset
    csv_loc = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    flight = pd.read_csv(csv_loc)

    data = []
    if hue == 'none':
        # membuat grup jika tidak ada hue/ colors
        if cat_x == 'year':
            flight = flight.groupby([cat_x]).sum().reset_index()

        # ambil semua data jika tanpa pembeda
        scatt = go.Scatter(
            x = flight[cat_x],
            y = flight[cat_y],
            mode = 'lines'
        )
        data.append(scatt)
    else:
        for val in flight[hue].unique():
            scatt = go.Scatter(
                x = flight[flight[hue] == val][cat_x],
                y = flight[flight[hue] == val][cat_y],
                mode = 'lines',
                name = val
            )
            data.append(scatt)
      

    layout = go.Layout(
        title= 'Line Plot',
        title_x= 0.5,
        xaxis=dict(title=cat_x),
        yaxis=dict(title=cat_y)
    )

    result = {"data": data, "layout": layout}
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


## Line PLOT Route ##
@app.route('/line_fn')
def line_fn():

    # mengambil nilai argumen dari API (saat awal akan None)
    cat_x = request.args.get('cat_x')  # ambil isi formulir dari html name: cat_x
    cat_y = request.args.get('cat_y')  # ambil isi formulir dari html name: cat_y
    hue = request.args.get('hue')    # ambil isi formulir dari html name: hue

    # WAJIB! default value ketika scatter pertama kali dipanggil
    if cat_x == None and cat_y == None and hue == None:
        cat_x = 'year'
        cat_y = 'passengers'
        hue = 'month'

    # Dropdown menu list
    list_x = [('year', 'Tahun'), ('month', 'Bulan')]
    list_y = [('passengers', 'Penumpang')]
    list_hue = [('none','None'), ('month', 'Month')]

    # kita panggil si plot nya
    plot = line_plot(cat_x, cat_y, hue)

    # render template html
    return render_template(
        'line.html',
        plot=plot,
        focus_x=cat_x,
        focus_y=cat_y,
        focus_hue=hue,
        drop_x= list_x,
        drop_y= list_y,
        drop_hue= list_hue,
    )


if __name__ == '__main__':
    app.run(debug=True)
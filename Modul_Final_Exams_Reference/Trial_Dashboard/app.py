# standard flask libraries
from os import name, sep
from flask import Flask, render_template, request
import pandas as pd
import json
import joblib

# visualization library
import plotly
import plotly.graph_objs as go

# custom library
from static.src.helpers import model_wo_preprocessor, Person, Model

# model = model_wo_preprocessor
# model1 = model_with_preprocessor

# data
sephora = pd.read_csv('./data/sephora.csv')
top5_brands = sephora['brand'].value_counts()[:5].index
sephora = sephora[sephora['brand'].isin(top5_brands)].reset_index(drop=True)


# print(model)

p = Person('Nikhil')
p.say_hi()

teks = 'Aku MENCOBA ga bilang #, > ? blm 😊 '
print(teks)
converter = Model(teks)
print(converter.text_preprocessing_with_stem(teks))

# route app
app = Flask(__name__)

# # ROUTE FUNCTION

# route to index.html
@app.route('/')
def index():
    return render_template('index.html', sephora=sephora)


if __name__ == '__main__':
    app.run(debug=True)


# # PLOT FUNCTION


# def category_plot(cat_plot='histplot', cat_x='brand', cat_y='price', estimator='count', hue='brand'):
#     title = ''
#     data = []
#     # SELECTION --> Histogram or Boxplot
#     if cat_plot == 'histplot':
#         for i in sephora[hue].unique():
#             hist = go.Histogram(
#                 x=sephora[sephora[hue] == i][cat_x],
#                 y=sephora[sephora[hue] == i][cat_y],
#                 histfunc=estimator,
#                 name=i
#             )
#             data.append(hist)
#         title = 'Histogram Sephora'
#     elif cat_plot == 'boxplot':
#         for i in sephora[hue].unique():
#             box = go.Box(
#                 x=sephora[sephora[hue] == i][cat_x],
#                 y=sephora[sephora[hue] == i][cat_y],
#                 name=i
#             )
#             data.append(box)
#         title == 'Box'

#     # SET x axis and y axis
#     if cat_plot == 'histplot':
#         layout = go.Layout(
#             title=title,
#             xaxis=dict(title=cat_x),
#             yaxis=dict(title='# Orders'),
#             boxmode='group'
#         )
#     else:
#         layout = go.Layout(
#             title=title,
#             xaxis=dict(title=cat_x),
#             yaxis=dict(title=cat_y),
#             boxmode='group'
#         )

#     result = {'data': data, 'layout': layout}
#     graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON


# def scatter_plot(cat_x, cat_y, hue, brand):

#     # call dataset
#     sephora = pd.read_csv('./data/sephora.csv')

#     # mapping brand
#     if brand == "SEPHORA_COLLECTION":
#         brand = "SEPHORA COLLECTION"
#     elif brand == "TOM_FORD":
#         brand = "TOM FORD"

#     # if brand all
#     if brand == 'all':
#         x = sephora
#         sephora = x[x['brand'].isin(top5_brands)]
#     else:
#         x = sephora
#         sephora = x[x['brand'] == brand]

#     data = []
#     for val in sephora[hue].unique():
#         scatt = go.Scatter(
#             x=sephora[sephora[hue] == val][cat_x],
#             y=sephora[sephora[hue] == val][cat_y],
#             mode='markers',
#             name=val
#         )
#         data.append(scatt)

#     layout = go.Layout(
#         title='Scatter',
#         title_x=0.5,
#         xaxis=dict(title=cat_x),
#         yaxis=dict(title=cat_y)
#     )

#     result = {"data": data, "layout": layout}
#     graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON


# def line_plot(cat_x, cat_y, hue):

#     # call dataset
#     csv_loc = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
#     flight = pd.read_csv(csv_loc)

#     data = []
#     if hue == 'none':
#         # membuat grup jika tidak ada hue/ colors
#         if cat_x == 'year':
#             flight = flight.groupby([cat_x]).sum().reset_index()

#         # ambil semua data jika tanpa pembeda
#         scatt = go.Scatter(
#             x=flight[cat_x],
#             y=flight[cat_y],
#             mode='lines'
#         )
#         data.append(scatt)
#     else:
#         for val in flight[hue].unique():
#             scatt = go.Scatter(
#                 x=flight[flight[hue] == val][cat_x],
#                 y=flight[flight[hue] == val][cat_y],
#                 mode='lines',
#                 name=val
#             )
#             data.append(scatt)

#     layout = go.Layout(
#         title='Line Plot',
#         title_x=0.5,
#         xaxis=dict(title=cat_x),
#         yaxis=dict(title=cat_y)
#     )

#     result = {"data": data, "layout": layout}
#     graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON


# # ROUTE FUNCTION

# # route to index.html
# @app.route('/')
# def index():
#     return render_template('index.html')

# # route to category.html
# @app.route('/category-plot/<nav>')
# def category_plot_route(nav):

#     # default value in initial click
#     if nav == "True":
#         cat_plot = 'histplot'
#         cat_x = 'category'
#         cat_y = 'number_of_reviews'
#         estimator = 'count'
#         hue = 'category'
#     # when selecting value from dropdown menu
#     else:
#         cat_plot = request.args.get('cat_plot')
#         cat_x = request.args.get('cat_x')
#         cat_y = request.args.get('cat_y')
#         estimator = request.args.get('estimator')
#         hue = request.args.get('hue')

#     # default value from boxplot to histogram will be None
#     if estimator == None:
#         estimator = 'count'
#     # when estimator == 'count', dropdown menu Y will be disabled and None
#     if cat_y == None:
#         cat_y = 'number_of_reviews'

#     # Dropdown menu [('input variables string','Label that show in drop down menu')]
#     list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
#     list_x = [('brand', 'Brand'), ('category', 'Category'),
#               ('price', 'Price'), ('love', 'Love')]
#     list_y = [('price', 'Price'), ('love', 'Love'),
#               ('number_of_reviews', 'Num Reviews')]
#     list_est = [('count', 'Count'), ('avg', 'Average'),
#                 ('max', 'Max'), ('min', 'Min')]
#     list_hue = [('brand', 'Brand'), ('category', 'Category')]

#     plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
#     return render_template(
#         "category_plot.html",
#         plot=plot,
#         focus_plot=cat_plot,
#         focus_x=cat_x, focus_y=cat_y,
#         focus_estimator=estimator,
#         focus_hue=hue,
#         drop_plot=list_plot,
#         drop_x=list_x, drop_y=list_y,
#         drop_estimator=list_est,
#         drop_hue=list_hue
#     )


# # route to scatter.html
# @app.route('/scatter-plot')
# def scatter_plot_route():

#     # mengambil nilai argumen dari API (saat awal akan None)
#     # ambil isi formulir dari html name: cat_x
#     cat_x = request.args.get('cat_x')
#     # ambil isi formulir dari html name: cat_y
#     cat_y = request.args.get('cat_y')
#     hue = request.args.get('hue')    # ambil isi formulir dari html name: hue
#     # ambil isi formulir dari html name: hue
#     brand = request.args.get('brand')

#     # WAJIB! default value ketika scatter pertama kali dipanggil
#     if cat_x == None and cat_y == None and hue == None:
#         cat_x = 'number_of_reviews'
#         cat_y = 'price'
#         hue = 'brand'
#         brand = 'all'

#     # Dropdown menu list
#     list_x = [('number_of_reviews', 'Num Reviews'),
#               ('price', 'Price'), ('love', 'Love')]
#     list_y = [('number_of_reviews', 'Num Reviews'),
#               ('price', 'Price'), ('love', 'Love')]
#     list_hue = [('brand', 'Brand')]
#     list_brand = [('all', 'All'), ('SEPHORA_COLLECTION', 'Sephora'), ('CLINIQUE',
#                                                                       'Clinique'), ('tarte', 'Tarte'), ('TOM_FORD', 'Tom Ford'),  ('Dior', 'Dior')]

#     # kita panggil si plot nya
#     plot = scatter_plot(cat_x, cat_y, hue, brand)

#     # render template html
#     return render_template(
#         'scatter.html',
#         plot=plot,
#         focus_x=cat_x,
#         focus_y=cat_y,
#         focus_hue=hue,
#         focus_brand=brand,
#         drop_x=list_x,
#         drop_y=list_y,
#         drop_hue=list_hue,
#         drop_brand=list_brand
#     )

# # route to line.html
# @app.route('/line-plot')
# def line_plot_route():

#     # mengambil nilai argumen dari API (saat awal akan None)
#     # ambil isi formulir dari html name: cat_x
#     cat_x = request.args.get('cat_x')
#     # ambil isi formulir dari html name: cat_y
#     cat_y = request.args.get('cat_y')
#     hue = request.args.get('hue')    # ambil isi formulir dari html name: hue

#     # WAJIB! default value ketika scatter pertama kali dipanggil
#     if cat_x == None and cat_y == None and hue == None:
#         cat_x = 'year'
#         cat_y = 'passengers'
#         hue = 'month'

#     # Dropdown menu list
#     list_x = [('year', 'Tahun'), ('month', 'Bulan')]
#     list_y = [('passengers', 'Penumpang')]
#     list_hue = [('none', 'None'), ('month', 'Month')]

#     # kita panggil si plot nya
#     plot = line_plot(cat_x, cat_y, hue)

#     # render template html
#     return render_template(
#         'line.html',
#         plot=plot,
#         focus_x=cat_x,
#         focus_y=cat_y,
#         focus_hue=hue,
#         drop_x=list_x,
#         drop_y=list_y,
#         drop_hue=list_hue,
#     )

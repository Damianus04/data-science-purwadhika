"""import plotly.graph_objs as go
import plotly
import json
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for
{{url_for('category_plot_route', nav=True)}}
{{url_for('scatter_plot_route')}}
{{url_for('line_plot_route')}}


# Default

# Visualization

# data
occupation = pd.read_csv('./data/occupation.csv', delimiter="|")
print(occupation.head())


app = Flask(__name__)

# PLOT


def scatter_plot(cat_x, cat_y):
    data = []
    scatt = go.Scatter(
        x=occupation[cat_x],
        y=occupation[cat_y],
        mode='markers',
    )

    layout = go.Layout(

    )

# ROUTE


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


def box_plot(x_axis='brand', y_axis='price'):
    data = [
        go.Box(
            x=sephora[x_axis],
            y=sephora[y_axis],
        )
    ]

    layout = go.Layout(
        title="Box Plot",
        xaxis=dict(title=x_axis),
        yaxis=dict(title=y_axis),
        boxmode='group'
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/boxplot')
def boxplot_route():
    # Request from dropdown menu
    x_axis = request.args.get('cat_x')  # x_axis = "brand"
    y_axis = request.args.get('cat_y')  # y_axis = "price"

    # x_axis = 'love'
    # y_axis = 'price'

    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('brand', 'Brand'), ('category', 'Category'),
              ('price', 'Price'), ('love', 'Love')]
    list_y = [('price', 'Price'), ('love', 'Love'),
              ('number_of_reviews', 'Num Reviews')]
    list_est = [('count', 'Count'), ('avg', 'Average'),
                ('max', 'Max'), ('min', 'Min')]
    list_hue = [('brand', 'Brand'), ('category', 'Category')]

    # Running bar_plot function
    box = box_plot(x_axis, y_axis)

    # return all variables
    return render_template('boxplot.html', plot=box,
                           focus_x=x_axis, focus_y=y_axis,
                           drop_plot=list_plot,
                           drop_x=list_x, drop_y=list_y,
                           drop_estimator=list_est, drop_hue=list_hue)


########################
@app.route('/boxplot', methods=["GET", 'POST'])
def boxplot_route():
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('brand', 'Brand'), ('category', 'Category'),
              ('price', 'Price'), ('love', 'Love')]
    list_y = [('price', 'Price'), ('love', 'Love'),
              ('number_of_reviews', 'Num Reviews')]
    list_est = [('count', 'Count'), ('avg', 'Average'),
                ('max', 'Max'), ('min', 'Min')]
    list_hue = [('brand', 'Brand'), ('category', 'Category')]

    if request.method == "GET":
        # Request from dropdown menu
        x_axis = request.args.get('cat_x')  # x_axis = "brand"
        y_axis = request.args.get('cat_y')  # y_axis = "price"

        # x_axis = 'love'
        # y_axis = 'price'

        # Running bar_plot function
        box = box_plot(x_axis, y_axis)

        # return all variables
        return render_template('boxplot.html', plot=box,
                               focus_x=x_axis, focus_y=y_axis,
                               drop_plot=list_plot,
                               drop_x=list_x, drop_y=list_y,
                               drop_estimator=list_est, drop_hue=list_hue)
    elif request.method == "POST":
        # Request from dropdown menu
        x_axis = request.args.get('cat_x')  # x_axis = "brand"
        y_axis = request.args.get('cat_y')  # y_axis = "price"

        # x_axis = 'love'
        # y_axis = 'price'

        # Running bar_plot function
        box = box_plot(x_axis, y_axis)

        # return all variables
        return render_template('boxplot.html', plot=box,
                               focus_x=x_axis, focus_y=y_axis,
                               drop_plot=list_plot,
                               drop_x=list_x, drop_y=list_y,
                               drop_estimator=list_est, drop_hue=list_hue)


def box_plot(x_axis='brand', y_axis='price'):
    data = [
        go.Box(
            x=sephora[x_axis],
            y=sephora[y_axis],
        )
    ]

    layout = go.Layout(
        title="Box Plot",
        xaxis=dict(title=x_axis),
        yaxis=dict(title=y_axis),
        boxmode='group'
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
"""

# standard flask libraries
from os import name, sep
from flask import Flask, render_template, request
import pandas as pd
import json

# visualization library
import plotly
import plotly.graph_objs as go

# data
sephora = pd.read_csv('./data/sephora.csv')
occupation = pd.read_csv('./data/occupation.csv', delimiter="|")


app = Flask(__name__)


# PLOT FUNCTION

def scatter_plot(x_axis='occupation', y_axis='age'):
    data = [
        go.Scatter(
            x=occupation[x_axis],
            y=occupation[y_axis],
            mode='markers'
        )
    ]

    layout = go.Layout(
        title='Scatter',
        title_x=0.5,
        xaxis=dict(title=x_axis),
        yaxis=dict(title=y_axis)
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


# ROUTE FUNCTION

# route to index.html
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scatter-plot')
def scatterplot_route():
    # x_axis = request.args.get('cat_x')
    # y_axis = request.args.get('cat_y')

    x_axis = 'gender'
    y_axis = 'age'

    list_x = [('age', 'Age'), ('gender', 'Gender'),
              ('occupation', 'Occupation'), ('zip_code', 'Zip_Code')]
    list_y = [('age', 'Age'), ('gender', 'Gender'),
              ('occupation', 'Occupation'), ('zip_code', 'Zip_Code')]

    # Running scatter_plot function
    bar = scatter_plot(x_axis, y_axis)

    # return all variables
    return render_template('scatterplot.html', plot=bar,
                           focus_x=x_axis, focus_y=y_axis,
                           drop_x=list_x, drop_y=list_y)


if __name__ == '__main__':
    app.run(debug=True)

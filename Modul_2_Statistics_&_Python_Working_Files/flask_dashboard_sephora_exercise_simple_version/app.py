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

app = Flask(__name__)


# PLOT FUNCTION

def scatter_plot(x_axis='brand', y_axis='price'):
    data = [
        go.Scatter(
            x=sephora[x_axis],
            y=sephora[y_axis],
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

# ROUTE FUNCTION

# route to index.html
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scatter-plot')
def scatterplot_route():
    # x_axis = request.args.get('cat_x')
    # y_axis = request.args.get('cat_y')

    x_axis = 'number_of_reviews'
    y_axis = 'price'

    list_x = [('brand', 'Brand'), ('category', 'Category'),
              ('price', 'Price'), ('love', 'Love')]
    list_y = [('price', 'Price'), ('love', 'Love'),
              ('number_of_reviews', 'Num Reviews')]

    # Running scatter_plot function
    bar = scatter_plot(x_axis, y_axis)

    # return all variables
    return render_template('scatterplot.html', plot=bar,
                           focus_x=x_axis, focus_y=y_axis,
                           drop_x=list_x, drop_y=list_y)


@app.route('/box-plot')
def boxplot_route():
    # x_axis = request.args.get('cat_x')
    # y_axis = request.args.get('cat_y')

    x_axis = 'price'
    y_axis = 'love'

    list_x = [('brand', 'Brand'), ('category', 'Category'),
              ('price', 'Price'), ('love', 'Love')]
    list_y = [('price', 'Price'), ('love', 'Love'),
              ('number_of_reviews', 'Num Reviews')]

    # Running scatter_plot function
    bar = box_plot(x_axis, y_axis)

    # return all variables
    return render_template('boxplot.html', plot=bar,
                           focus_x=x_axis, focus_y=y_axis,
                           drop_x=list_x, drop_y=list_y)


if __name__ == '__main__':
    app.run(debug=True)

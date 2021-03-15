# standard flask libraries
from os import name, sep
from flask import Flask, render_template, request
import pandas as pd
import json

# visualization library
import plotly
import plotly.graph_objs as go

# data
real_estate = pd.read_csv('./data/melb_data.csv')
app = Flask(__name__)


# PLOT FUNCTION


def box_plot(x_axis='Distance'):
    data = [
        go.Box(
            x=real_estate[x_axis],
        )
    ]

    layout = go.Layout(
        title="Box Plot",
        xaxis=dict(title=x_axis),
        boxmode='group'
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def line_plot(x_axis='YearBuilt', y_axis='Price'):
    data = [
        go.Scatter(
            x=real_estate[x_axis],
            y=real_estate[y_axis],
            mode='lines+markers'
        )
    ]

    layout = go.Layout(
        title="Line Plot",
        xaxis=dict(title=x_axis),
        yaxis=dict(title=y_axis),
        title_x=0.5
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# ROUTE FUNCTION

# route to index.html
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/dataset")
def dataset_route():
    table = real_estate.head(100)
    return render_template('dataset.html', data=table)


@app.route('/box-plot')
def boxplot_route():
    # x_axis = request.args.get('cat_x')
    # y_axis = request.args.get('cat_y')

    x_axis = 'Distance'

    list_x = [('Distance', 'Distance')]

    # Running scatter_plot function
    bar = box_plot(x_axis)

    # return all variables
    return render_template('boxplot.html', plot=bar,
                           focus_x=x_axis,
                           drop_x=list_x)


@app.route('/line-plot')
def lineplot_route():

    x_axis = request.args.get('cat_x')
    y_axis = request.args.get('cat_y')

    # x_axis = 'YearBuilt'
    # y_axis = 'Price'

    list_x = [('YearBuilt', 'Year Built'), ('Price', 'Price')]
    list_y = [('Price', 'Price'), ('YearBuilt', 'Year Built')]

    # Running scatter_plot function
    line = line_plot(x_axis, y_axis)

    # return all variables
    return render_template('lineplot.html', plot=line,
                           focus_x=x_axis, focus_y=y_axis,
                           drop_x=list_x, drop_y=list_y)

# @app.route('/line-plot')
# def lineplot_route():
#     # x_axis = request.args.get('cat_x')
#     # y_axis = request.args.get('cat_y')

#     x_axis = 'YearBuilt'
#     y_axis = 'Price'

#     list_x = [('YearBuilt', 'Year Built')]
#     list_y = [('Price', 'Price')]

#     # Running scatter_plot function
#     line = line_plot(x_axis, y_axis)

#     # return all variables
#     return render_template('lineplot.html', plot=line,
#                            focus_x=x_axis, focus_y=y_axis,
#                            drop_x=list_x, drop_y=list_y)


if __name__ == '__main__':
    app.run(debug=True, port=5005)

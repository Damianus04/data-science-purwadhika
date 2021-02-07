# standard flask libraries
from os import name, sep
from flask import Flask, render_template, request
import pandas as pd
import json

# visualization library
import plotly
import plotly.graph_objs as go

# data
occupation = pd.read_csv('./data/occupation.csv', delimiter="|")


app = Flask(__name__)


def bar_plot(x_axis='occupation', y_axis='age'):
    data = [
        go.Scatter(
            x=occupation[x_axis],
            y=occupation[y_axis],
            mode='markers'
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def box_plot(x_axis='occupation', y_axis='age'):
    data = [
        go.Scatter(
            x=occupation[x_axis],
            y=occupation[y_axis],
            mode='markers'
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# ROUTE FUNCTION

# route to index.html
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/barplot')
def barplot_route():
    # Request from dropdown menu
    x_axis = request.args.get('cat_x')  # x_axis = "occupation"
    y_axis = request.args.get('cat_y')  # y_axis = "age"

    # Dropdown menu [('input variables string','Label that show in drop down menu')]
    list_plot = [('barplot', 'Barplot'), ('boxplot', 'Box')]
    list_x = [('age', 'Age'), ('gender', 'Gender'),
              ('occupation', 'Occupation'), ('zip_code', 'Zip_Code')]
    list_y = [('age', 'Age'), ('gender', 'Gender'),
              ('occupation', 'Occupation'), ('zip_code', 'Zip_Code')]
    list_est = [('count', 'Count'), ('avg', 'Average'),
                ('max', 'Max'), ('min', 'Min')]
    list_hue = [('gender', 'Gender')]

    # Running bar_plot function
    bar = bar_plot(x_axis, y_axis)

    # return all variables
    return render_template('barplot.html', plot=bar,
                           focus_x=x_axis, focus_y=y_axis,
                           drop_plot=list_plot,
                           drop_x=list_x, drop_y=list_y,
                           drop_estimator=list_est, drop_hue=list_hue)


@app.route('/barplot')
def boxplot_route():
    # Request from dropdown menu
    x_axis = request.args.get('cat_x')  # x_axis = "occupation"
    y_axis = request.args.get('cat_y')  # y_axis = "age"

    # Dropdown menu [('input variables string','Label that show in drop down menu')]
    list_plot = [('barplot', 'Barplot'), ('boxplot', 'Box')]
    list_x = [('age', 'Age'), ('gender', 'Gender'),
              ('occupation', 'Occupation'), ('zip_code', 'Zip_Code')]
    list_y = [('age', 'Age'), ('gender', 'Gender'),
              ('occupation', 'Occupation'), ('zip_code', 'Zip_Code')]
    list_est = [('count', 'Count'), ('avg', 'Average'),
                ('max', 'Max'), ('min', 'Min')]
    list_hue = [('gender', 'Gender')]

    # Running bar_plot function
    bar = bar_plot(x_axis, y_axis)

    # return all variables
    return render_template('boxplot.html', plot=bar,
                           focus_x=x_axis, focus_y=y_axis,
                           drop_plot=list_plot,
                           drop_x=list_x, drop_y=list_y,
                           drop_estimator=list_est, drop_hue=list_hue)


if __name__ == '__main__':
    app.run()

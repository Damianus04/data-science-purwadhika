# Default
from flask import Flask, render_template, request, url_for
import numpy as np
import pandas as pd
import json

# Visualization
import plotly
import plotly.graph_objs as go


app = Flask(__name__)
sephora = pd.read_csv('data/sephora_website_dataset_top_5.csv')
# print(sephora['price'])

# Index.html
@app.route('/')
def index():
    return render_template('index.html', data=sephora.head())


# BOXPLOT
# render boxplot.html belum bisa keluar

def boxplot():
    data = [
        go.Box(
            x=sephora['brand'],
            y=sephora['price']
        )
    ]
    title = 'Box Plot'

    layout = go.Layout(
        title=title,
        xaxis=dict(title='brand'),
        yaxis=dict(title='price'),
        boxmode='group'
    )

    result = {'data': data, 'layout': layout}
    brand = sephora.head()
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON, brand


@app.route('/price-distribution', methods=["GET", 'POST'])
def price_distribution():
    data = sephora.columns
    box = boxplot()
    if request.method == "GET":
        return render_template('price-distribution.html', plot=box, text=data)
    elif request.method == "POST":
        # box = boxplot()
        return render_template('price-distribution.html', plot=box, text=data)


if __name__ == '__main__':
    app.run(debug=True)

# Default
from flask import Flask, render_template, request, url_for
import numpy as np
import pandas as pd
import json

# Visualization
import plotly as px
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

    brand = sephora.head()
    graphJSON = json.dumps(data, cls=px.utils.PlotlyJSONEncoder)

    return graphJSON, brand


@app.route('/price-distribution')
def price_distribution():
    box = boxplot()
    return render_template('boxplot.html', plot=box)


if __name__ == '__main__':
    app.run(debug=True)

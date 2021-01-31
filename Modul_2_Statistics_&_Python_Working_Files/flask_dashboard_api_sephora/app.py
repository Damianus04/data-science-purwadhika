# Default
from flask import Flask, render_template, request, url_for
import numpy as np
import pandas as pd
import json

# Visualization
import plotly
import plotly.graph_objs as go


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

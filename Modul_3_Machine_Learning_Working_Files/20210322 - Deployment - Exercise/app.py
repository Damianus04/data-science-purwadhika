from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/visualize', methods=['POST', "GET"])
def visual():
    return render_template('plot.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict_html')


@app.route('/result', methods=["POST", 'GET'])
def result():
    if request.method == "POST":
        user = request.form

        df_to_predict = pd.Dataframe({
            'alcohol': [user['Alcohol']],
            'density': [user['Density']],
            'fixed_acidity': [user['Acidity']],
            'chlorides': [user['Chlorides']]
        })

        prediksi = model.predict(df_to_predict)

        if prediksi == 0:
            quality = 'Bad'
        else:
            quality = 'Good'

        return render_template('result.html', data=user, pred=quality)


if __name__ == '__main__':
    filename = 'model/logit_final.sav'
    model = pickle.load(open(filename, 'rb'))

    app.run(debug=True, port=1234)

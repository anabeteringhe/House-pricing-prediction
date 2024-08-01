import pandas as pd
import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\Ana\Desktop\House-pricing-prediction-master\Site\PY\server\predict"))
from predict import *
from flask import Flask, request, Response

from graphgenerator import *
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

createPlots()
etModel = ExtraTreesTrain()
rfModel = randForestTrain()

@app.route("/calculated", methods=['GET', 'POST'])
def calculatedPost():
    if request.method == 'GET':
        return Response(json.dumps("Salut"))
    
    if request.method == 'POST':
        data = request.json
        dataDf = {"Suprafata utila": data[0], "Tip incalzire": data[1], "Suprafata teren (m2)": data[2],
                  "Anul constructiei": data[3], "Numarul de camere": data[4], "Aer conditionat": data[5]}

        predictDf = pd.DataFrame(data = dataDf, index=[1])
        returnDataEt = predict_model(etModel, data = predictDf)
        returnDataRf = predict_model(rfModel, data = predictDf)

        dataEt, dataRf = returnDataEt.prediction_label, returnDataRf.prediction_label

        if(dataEt[1] > dataRf[1]):
            return Response(json.dumps(dataRf[1]))
        else:
            return Response(json.dumps(dataEt[1]))


if __name__ == '__main__':
    app.run(port=7000)
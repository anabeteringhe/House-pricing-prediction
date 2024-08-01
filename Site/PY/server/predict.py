from unidecode import unidecode
import pandas as pd

df = pd.read_csv(r"C:\Users\Ana\Desktop\House-pricing-prediction-master\CSVs\EditedData_dfShort-cap.csv", encoding="utf-16")

for col in df:
    df.rename(columns = {col:unidecode(col)}, inplace = True)

data = df.sample(frac=1).reset_index(drop=True)
print('Data for Modeling: ' + str(data.shape))

from pycaret.regression import *

exp_reg101 = setup(data = data, target = 'Pret') 

def randForestTrain():
    rf = create_model('rf')
    tuned_rf = tune_model(rf)
    final_rf = finalize_model(tuned_rf)
    return final_rf

def ExtraTreesTrain():
    et = create_model('et')
    tuned_et = tune_model(et)
    final_et = finalize_model(tuned_et)
    return final_et
# -*- coding: utf-8 -*-
"""fertpred.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yNhIBRoO8ZqP-XJj8dNlMTL55biXUFkQ
"""

from __future__ import print_function
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
import sys

warnings.filterwarnings('ignore')


def fertrec():
    df = pd.read_csv('Fertilizer Prediction.csv')

    from sklearn import preprocessing

    # label_encoder object knows how to understand word labels.
    label_encoder = preprocessing.LabelEncoder()
    # Encode labels in column 'species'.
    df['Soil Type'] = label_encoder.fit_transform(df['Soil Type'])
    df['Crop Type'] = label_encoder.fit_transform(df['Crop Type'])
    features = df[
        ['Temparature', 'Humidity ', 'Moisture', 'Soil Type', 'Crop Type', 'Nitrogen', 'Potassium', 'Phosphorous']]
    target = df['Fertilizer Name']
    # features = df[['temperature', 'humidity', 'ph', 'rainfall']]
    labels = df['Fertilizer Name']
    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(features, target, test_size=0.2, random_state=2)
    from sklearn.ensemble import RandomForestClassifier

    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    sv = RF.fit(Xtrain, Ytrain)
    temp = sys.argv[1]
    hum = sys.argv[2]
    mois = sys.argv[3]
    soiltype = sys.argv[4]
    if soiltype=='Sandy':
        soiltype=4
    elif soiltype=='Loamy':
        soiltype=2
    elif soiltype=='Black':
        soiltype=0
    elif soiltype=='Red':
        soiltype=3
    elif soiltype=='Clayey':
        soiltype=1
    croptype = sys.argv[5]
    N = sys.argv[6]
    Potash = sys.argv[7]
    phos = sys.argv[8]
    if croptype=='Maize':
        croptype=3
    elif croptype=='Sugarcane':
        croptype=8
    elif croptype=='Cotton':
        croptype=1
    elif croptype=='Tobacco':
        croptype=9
    elif croptype=='Paddy':
        croptype=6
    elif croptype=='Barley':
        soiltype=0
    elif croptype=='Wheat':
        croptype=10
    elif croptype=='Millets':
        croptype=4
    elif croptype=='Oil seeds':
        croptype=5
    elif croptype=='Pulses':
        croptype=7
    elif croptype=='Ground Nuts':
        croptype=2

    data = np.array([[temp, hum, mois, soiltype, croptype, N, Potash, phos]])
    prediction = RF.predict(data)
    print(prediction)
    pickle.dump(sv, open('fertpred.pkl', 'wb'))


if __name__ == '__main__':
    fertrec()

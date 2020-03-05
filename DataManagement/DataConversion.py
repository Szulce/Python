import json

import matplotlib as matplotlib
import matplotlib.pyplot as plot_view
import numpy
import pandas
import numpy as np
import sklearn
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import Imputer

features_all = ['id',  # patient identification number
                'ccf',  # social security number (I replaced this with a dummy value of 0)
                'age',  # age in years
                'sex',  # sex (1 = male; 0 = female)
                'painloc',  # chest pain location (1 = substernal; 0 = otherwise)
                'painexer',  # (1 = provoked by exertion; 0 = otherwise)
                'relrest',  # (1 = relieved after rest; 0 = otherwise)
                'pncaden',  # (sum of 5, 6, and 7)
                'cp',  # chest pain type
                # -- Value 1: typical angina
                # -- Value 2: atypical angina
                # -- Value 3: non-anginal pain
                # -- Value 4: asymptomatic
                'trestbps',  # resting blood pressure (in mm Hg on admission to the hospital)
                'htn',
                'chol',  # serum cholestoral in mg/dl
                'smoke',  # I believe this is 1 = yes; 0 = no (is or is not a smoker)
                'cigs',  # (cigarettes per day)
                'years',  # (number of years as a smoker)
                'fbs',  # (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
                'dm',  # (1 = history of diabetes; 0 = no such history)
                'famhist',  # family history of coronary artery disease (1 = yes; 0 = no)
                'restecg',  # resting electrocardiographic results
                # -- Value 0: normal
                # -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
                # -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
                'ekgmo',  # (month of exercise ECG reading)
                'ekgday',  # (day of exercise ECG reading)
                'ekgyr',  # (year of exercise ECG reading)
                'dig',  # (digitalis used furing exercise ECG: 1 = yes; 0 = no)
                'prop',  # (Beta blocker used during exercise ECG: 1 = yes; 0 = no)
                'nitr',  # (nitrates used during exercise ECG: 1 = yes; 0 = no)
                'pro',  # (calcium channel blocker used during exercise ECG: 1 = yes; 0 = no)
                'diuretic',  # (diuretic used used during exercise ECG: 1 = yes; 0 = no)
                'proto',  # exercise protocol
                # 1 = Bruce
                # 2 = Kottus
                # 3 = McHenry
                # 4 = fast Balke
                # 5 = Balke
                # 6 = Noughton
                # 7 = bike 150 kpa min/min (Not sure if "kpa min/min" is what was written!)
                # 8 = bike 125 kpa min/min
                # 9 = bike 100 kpa min/min
                # 10 = bike 75 kpa min/min
                # 11 = bike 50 kpa min/min
                # 12 = arm ergometer
                'thaldur',  # duration of exercise test in minutes
                'thaltime',  # time when ST measure depression was noted
                'met',  # mets achieved
                'thalach',  # maximum heart rate achieved
                'thalrest',  # resting heart rate
                'tpeakbps',  # peak exercise blood pressure (first of 2 parts)
                'tpeakbpd',  # peak exercise blood pressure (second of 2 parts)
                'dummy',  #
                'trestbpd',  # resting blood pressure
                'exang',  # exercise induced angina (1 = yes; 0 = no)
                'xhypo',  # (1 = yes; 0 = no)
                'oldpeak',  # = ST depression induced by exercise relative to rest
                'slope',  # the slope of the peak exercise ST segment
                # -- Value 1: upsloping
                # -- Value 2: flat
                # -- Value 3: downsloping
                'rldv5',  # height at rest
                'rldv5e',  # height at peak exercise
                'ca',  # number of major vessels (0-3) colored by flourosopy
                'restckm',  # irrelevant
                'exerckm',  # irrelevant
                'restef',  # rest raidonuclid (sp?) ejection fraction
                'restwm',  # rest wall (sp?) motion abnormality
                # 0 = none
                # 1 = mild or moderate
                # 2 = moderate or severe
                # 3 = akinesis or dyskmem (sp?)
                'exeref',  # exercise radinalid (sp?) ejection fraction
                'exerwm',  # exercise wall (sp?) motion
                'thal',  # 3 = normal; 6 = fixed defect; 7 = reversable defect
                'thalsev',  # not used
                'thalpul',  # not used
                'earlobe',  # not used
                'cmo',  # month of cardiac cath (sp?) (perhaps "call")
                'cday',  # day of cardiac cath (sp?)
                'cyr',  # year of cardiac cath (sp?)
                'num',  # diagnosis of heart disease (angiographic disease status)
                # -- Value 0: < 50% diameter narrowing
                # -- Value 1: > 50% diameter narrowing
                # (in any major vessel: attributes 59 through 68 are vessels)
                'lmt',  #
                'ladprox',  #
                'laddist',  #
                'diag',  #
                'cxmain',  #
                'ramus',  #
                'om1',  #
                'om2',  #
                'rcaprox',  #
                'rcadist',  #
                'lvx1',  # not used
                'lvx2',  # not used
                'lvx3',  # not used
                'lvx4',  # not used
                'lvf',  # not used
                'cathef',  # not used
                'junk',  # not used
                'name',  # last name of patient (I replaced this with the dummy string "name")
                ]

features_used = ['age',  # 3
                 'sex',  # 4
                 'cp',  # 9
                 'trestbps',  # 10
                 'chol',  # 12
                 'fbs',  # 16
                 'restecg',  # 19
                 'thalach',  # 32
                 'exang',  # 38
                 'oldpeak',  # 40
                 'slope',  # 41
                 'ca',  # 44
                 'thal',  # 51
                 'num',  # 58
                 ]
# 63.0 ,   1.0,  1.0,  145.0, 233.0, 1.0, 2.0,150.0,0.0,2.3,3.0,0.0,6.0,0
# 63 lat , men, angina, mmHG, chol, sugar,
load_files = []
data_frame = []


def read():
    data_directory_path = 'DataManagement/'
    data_files = ['processed.cleveland.data', 'processed.hungarian.data', 'processed.switzerland.data',
                  'processed.va.data']

    for filename in data_files:
        data_from_file = pandas.read_csv(data_directory_path + filename, sep=',', index_col=None, header=None,
                                         names=features_used, keep_default_na=False, na_values='?')
        load_files.append(data_from_file)

    global data_frame
    data_frame = pandas.concat(load_files, axis=0, ignore_index=True)

    # data_frame.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
    # plot_view.show()

    data_frame = pandas.DataFrame(data_frame, columns=features_used)
    imputed = Imputer(strategy="mean", missing_values=numpy.NaN)
    imputed = imputed.fit(data_frame)
    data_frame = imputed.transform(data_frame)
    # data_frame = data_frame.reshape(920, 14)
    print(data_frame)
    # print(data_frame.shape)
    # print(data_frame.describe())

    # scatter_matrix(data_frame)
    # plot_view.show()


read()


# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Citation Request:

# The authors of the databases have requested that any publications resulting from the use of the data include the names of the principal investigator responsible for the data collection at each institution. They would be:
# 1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
# 2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
# 3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
# 4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:Robert Detrano, M.D., Ph.D.

def savePredictionToJson(prediction, algorithm):
    if algorithm == 'AUTO':
        with open('DataManagement/results/Auto.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'TREE':
        with open('DataManagement/results/Tree.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'SVM':
        with open('DataManagement/results/Svm.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'KNN':
        with open('DataManagement/results/Knn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()


def savePredictionWithPicke(prediction, algorithm):
    if algorithm == 'AUTO':
        with open('DataManagement/results/Auto.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'TREE':
        with open('DataManagement/results/Tree.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'SVM':
        with open('DataManagement/results/Svm.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'KNN':
        with open('DataManagement/results/Knn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()


def readPrediction(algorithm):
    all_predictions = []
    if algorithm == 'AUTO' or algorithm == 'ALL':
        with open('DataManagement/results/Auto.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'TREE' or algorithm == 'ALL':
        with open('DataManagement/results/Tree.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'SVM' or algorithm == 'ALL':
        with open('DataManagement/results/Svm.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'KNN' or algorithm == 'ALL':
        with open('DataManagement/results/Knn.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    return all_predictions


def getModel():
    return "Model"

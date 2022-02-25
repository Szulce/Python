import numpy
from sklearn.impute import SimpleImputer

# LogConfig
PREDICTION_MANAGEMENT_ = '/PredictionManagement/'
NUMPY = "Numpy"
PANDAS = "Pandas"
K_FOLD = "K-fold"
SCIKIT_LEARN = "Scikit-learn"
ARCH_FILE_NAME = 'Arch.zip'
LOG_FILES_DIRECTORY = 'Config/LogFiles'
LOG_FILE_NAME = "UMNWWCHS.log"

# Model Storage
RF___SAV = "Rf1.sav"
RF_TYPE_DIRECTORY = "/Rf"

SVN___SAV = "Svn1.sav"
SVN_TYPE_DIRECTORY = "/Svn"

KNN___SAV = "Knn1.sav"
KNN_TYPE_DIRECTORY = "/Knn"

AUTO___SAV = "Auto1.sav"
AUTO_TYPE_DIRECTORY = "/Auto"

MODULE_DIRECTORY_PATH = 'ComparativeSupervisedLearning%s' % PREDICTION_MANAGEMENT_

SAV_DIR = "/Sav/"

KNN_FULL_PATH_SAV = MODULE_DIRECTORY_PATH + KNN_TYPE_DIRECTORY + SAV_DIR + KNN___SAV
SVN_FULL_PATH_SAV = MODULE_DIRECTORY_PATH + SVN_TYPE_DIRECTORY + SAV_DIR + SVN___SAV
RF_FULL_PATH_SAV = MODULE_DIRECTORY_PATH + RF_TYPE_DIRECTORY + SAV_DIR + RF___SAV

MODEL_TYPE_KNN = "Knn"
MODEL_TYPE_SVN = "Svn"
MODEL_TYPE_RF = "Rf"
MODEL_TYPE_AUTO = "Auto"

MODELS = [MODEL_TYPE_KNN, MODEL_TYPE_SVN, MODEL_TYPE_RF, MODEL_TYPE_AUTO]

SLESH = "\\"

# Data Conversion


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
                'restecg',  # resting electrocardiographic JsonResult
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

features_prediction = ['age',  # 3
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
                                  ]

features_used_categorical = [
    'slope',  # 41
    'ca',  # 44
    'thal',  # 51
]

features_used_numerical = ['age', 'trestbps', 'chol', 'restecg', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']

# Data Conversion PreProcessing
imputed_mean = SimpleImputer(strategy="mean", missing_values=numpy.NaN, fill_value=-1)
# , add_indicator=True)
imputed_median = SimpleImputer(strategy="median", missing_values=numpy.NaN, fill_value=-1)
# , add_indicator=True)
imputed_most_frequent = SimpleImputer(strategy="most_frequent", missing_values=numpy.NaN, fill_value=-1)
imputed_most_constant = SimpleImputer(strategy="constant", missing_values=numpy.NaN, fill_value=-1)

IMPUTERS_LIST = [
    imputed_mean, imputed_median,
    imputed_most_constant
    , imputed_most_frequent
]

# Data Conversion split data
SPLIT_METHODS = [SCIKIT_LEARN, NUMPY, K_FOLD]
SCIKIT_test_size = 0.1
SCIKIT_random_state = 53
PANDAS_frac = 0.8
PANDAS_random_state = 1
NUMPY_mask = 0.8

# knn
N_NEIGHBORS_SIZE = 14
N_NEIGHBORS = "n_neighbors"
KNN_GRID_SPLITER = 7

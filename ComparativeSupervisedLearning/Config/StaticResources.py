import numpy
from sklearn import metrics
from sklearn.impute import SimpleImputer

"""" Store Static resources for example: paths, names of files, names of types   """

# LogConfig
PREDICTION_MANAGEMENT_ = '\Management\Prediction\\'
PREDICTION_ELABORATION_ = '\Management\PlotGeneration\PlotsObjects\\'
NUMPY = "Numpy"
PANDAS = "Pandas"
K_FOLD = "K-fold"
SCIKIT_LEARN = "Scikit-learn"
ARCH_FILE_NAME = 'Arch.zip'
LOG_FILES_DIRECTORY = 'Config/LogFiles'
LOG_FILE_NAME = "UMNWWCHS_fr_cls.log"

# Model Storage
RF___SAV = "Rf1.sav"
RF_TYPE_DIRECTORY = "/Rf"

SVM___SAV = "Svm1.sav"
SVM_TYPE_DIRECTORY = "/Svm"

KNN___SAV = "Knn1.sav"
KNN_TYPE_DIRECTORY = "/Knn"

AUTO___SAV = "Auto1.sav"
AUTO_TYPE_DIRECTORY = "/Auto"

MODULE_DIRECTORY_PATH = 'ComparativeSupervisedLearning%s' % PREDICTION_MANAGEMENT_

SAV_DIR = "/Sav/"

KNN_FULL_PATH_SAV = MODULE_DIRECTORY_PATH + KNN_TYPE_DIRECTORY + SAV_DIR + KNN___SAV
SVN_FULL_PATH_SAV = MODULE_DIRECTORY_PATH + SVM_TYPE_DIRECTORY + SAV_DIR + SVM___SAV
RF_FULL_PATH_SAV = MODULE_DIRECTORY_PATH + RF_TYPE_DIRECTORY + SAV_DIR + RF___SAV

MODEL_TYPE_KNN = "Knn"
MODEL_TYPE_SVM = "Svm"
MODEL_TYPE_RF = "Rf"
MODEL_TYPE_AUTO = "Auto"

MODELS = [MODEL_TYPE_KNN, MODEL_TYPE_SVM, MODEL_TYPE_RF]  # , MODEL_TYPE_AUTO]

SLASH = "\\"

DATA_INFO_PLOTS = "data_info_plots"
ALGORITHM_INFO_PLOTS = "algorithm_info_plots"
SCORER_MODEL = "_scorer_model"

VERBOSE = 1

RF_ = ' \nRF : \n'

SVM_ = ' \nSVM : \n'

KNN_ = ' \nKNN : \n'

OUT_JSON_RESULT_ = 'C:/Users/User/PycharmProjects/Python/ComparativeSupervisedLearning/Data/Dto/Out/JsonResult/'

# In Conversion

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

# In Conversion PreProcessing
imputed_mean = SimpleImputer(strategy="mean", missing_values=numpy.NaN, fill_value=-1)
imputed_median = SimpleImputer(strategy="median", missing_values=numpy.NaN, fill_value=-1)
imputed_most_frequent = SimpleImputer(strategy="most_frequent", missing_values=numpy.NaN, fill_value=-1)
imputed_most_constant = SimpleImputer(strategy="constant", missing_values=numpy.NaN, fill_value=-1)

IMPUTERS_LIST = [
    imputed_mean, imputed_median,
    imputed_most_constant
    , imputed_most_frequent
]

# In Conversion split data
SPLIT_METHODS = [SCIKIT_LEARN, NUMPY, K_FOLD]
SCIKIT_test_size = 0.2
SCIKIT_random_state = 52
PANDAS_frac = 0.8
PANDAS_random_state = 1
NUMPY_mask = 0.8

# knn
N_NEIGHBORS_SIZE = 14
N_NEIGHBORS = "n_neighbors"
KNN_GRID_SPLITER = 7
KNN_WEIGHTS = ['uniform', 'distance']
KNN_ALGORITHM = ['auto', 'brute']
# , 'kd_tree'

KNN_LEAF_SIZE = [1, 5, 100]  # leaf_size <= n_points <= 2 * leaf_size
KNN_P_PARAM = [1, 1.5, 2]
KNN_METRIC = ['minkowski', 'chebyshev', 'manhattan',
              'hamming', 'canberra', 'braycurtis', 'jaccard', 'matching', 'dice', 'kulsinski', 'sokalmichener']
KNN_METRIC_PARAMS = {'w': [numpy.array([2.0] * N_NEIGHBORS_SIZE)], 'p': KNN_P_PARAM}

# svm
SVM_C = [0.1, 0.05, 1, 100]
SVM_GAMMA = ['scale', 'auto']
SVM_KERNEL = ['linear', 'poly', 'rbf', 'sigmoid']  # kernels = ['Polynomial', 'RBF', 'Sigmoid','Linear','precomputed']
SVM_DEGREE = [1, 3, 5]
SVM_COE0FLOAT = [0.0, 0.1, 0.3]
SVM_EPSILON = [0.1, 0.25, 0.3]
SVM_SHRINKING = [True, False]
SVM_CACHE_SIZE = [200, 500]
CLASS_WEIGHT=[None,'balanced']
# rf
RF_MAX_DEPTH = [5, 7, 13]
RF_RANDOM_STATE = [0, 2, 27]
RF_MAX_FEATURES = [None, 'auto', 'sqrt', 'log2']
RF_CRITERION = ['gini', 'entropy']
RF_SPLITTER = ['best', 'random']
RF_MIN_SAMPLES = [1.1, 2.0, 5.0]
RF_MIN_SAMPLES_LEAF = [1, 2, 5]
RF_MIN_WEIGHT_FRACTION_LEAF = [0.0, 0.1, 0.25]
RF_MIN_IMPURITY_DECREASE = [0.0, 0.25]
RF_CPP = [0.0, 0.25]
RF_N_ESTIMATORS = [10, 50, 100]
CV = 10

COLUMNS = {"age": "wiek", "sex": "plec", "cp": "bol_w_klatce_piersiowej", "trestbps": "cisnienie_krwi",
           "fbs": "cukier", "chol": "cholesterol", "num": "wynik"}

macro_precision = metrics.make_scorer(metrics.precision_score, average='macro')
macro_average_precision = metrics.make_scorer(metrics.average_precision_score, average='macro')
accuracy_scorer = metrics.make_scorer(metrics.accuracy_score)
balanced_accuracy_scorer = metrics.make_scorer(metrics.balanced_accuracy_score)
r2_score = metrics.make_scorer(metrics.r2_score)
macro_recall = metrics.make_scorer(metrics.recall_score, average='macro')
SCORER_DICTIONARY = dict(
    precision=macro_precision,
    average_precision=macro_average_precision,
    recall=macro_recall,
    balanced_accuracy=balanced_accuracy_scorer,
    r2=r2_score,
    accuracy=accuracy_scorer)

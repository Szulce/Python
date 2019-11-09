import autosklearn.classification
import sklearn.model_selection
import sklearn.metrics
from pandas import read_csv
from numpy import set_printoptions
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from DataManagement import DataConversion

x = None
y = None
prediction_test_size = 0.2
seed = 151515


def data_prepare():
    global x, y
    DataConversion.read()
    x = DataConversion.data_frame[:, 1:12]
    y = DataConversion.data_frame[:, 13]


import numpy as np


def run_1():
    data_prepare()
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        x,
        y,
        test_size=prediction_test_size, random_state=seed)
    auto_model = autosklearn.classification.AutoSklearnClassifier()
    auto_model.fit(np.asanyarray(range(0, 10)).reshape(-1, 1),
                   np.asanyarray([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]).reshape(-1, 1))
    # prediction = auto_model.predict(x_test)
    print("fit end")
    # DataConversion.savePrediction(prediction, 'AUTO')
    # accuracy = sklearn.metrics.accuracy_score(y_test, prediction)
    # print("ACCURACY %.3f%%") % (accuracy * 100.0)
    # return accuracy


def run_2():
    data_prepare()
    x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=prediction_test_size, random_state=seed)

    model_1 = RandomForestClassifier(n_estimators=10000,
                                     random_state=seed,
                                     max_features='log2',
                                     n_jobs=-1, verbose=1)
    model_2 = SVC()
    model_3 = KNeighborsClassifier()

    model_1.fit(x_train, y_train)
    result_1 = model_1.score(x_test, y_test)
    # print("ACCURACY %.3f%%") % (result_1 * 100.0)
    print("accuracy : ", result_1)
    n_nodes = []
    max_d = []

    # Stats about the trees in random forest
    for tree in model_1.estimators_:
        n_nodes.append(tree.tree_.node_count)
        max_d.append(tree.tree_.max_depth)
    print(f'nodes {n_nodes}')
    print(f'maximum depth {max_d}')

    # ważność cechy
    list(zip(x_train, model_1.feature_importances_))

    DataConversion.savePrediction(result_1, 'AUTO')

    model_2.fit(x_train, y_train)
    result_2 = model_2.score(x_test, y_test)
    # print("ACCURACY %.3f%%") % (result_2 * 100.0)
    print("accuracy : ", result_2)
    DataConversion.savePrediction(result_2, 'AUTO')

    model_3.fit(x_train, y_train)
    result_3 = model_3.score(x_test, y_test)
    # print("ACCURACY %.3f%%") % (result_3 * 100.0)
    print("accuracy : ", result_3)
    DataConversion.savePrediction(result_3, 'AUTO')
    return [result_1, result_2, result_3]

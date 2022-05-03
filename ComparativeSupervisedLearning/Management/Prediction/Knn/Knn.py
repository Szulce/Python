import time

import numpy
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" K nearest neighbours algorithm performance """


def create_train_save_model(x_train, x_test, y_train, y_test, iterator):
    grid, y_train, y_test = prepare_grid_classification(y_train, y_test)
    start_time = time.time()
    grid_fitted = grid.fit(x_train, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    y_predict = grid_fitted.predict(x_test)
    score = grid_fitted.best_score_ * 100
    # print(classification_report(y_test, y_predict))
    Ms.save_grid_scores(grid_fitted, Rs.MODEL_TYPE_KNN, iterator)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        Plot.create_measure_table(score, y_predict, y_test, exec_time),
        Rs.MODEL_TYPE_KNN, iterator)


def create_train_save_regression_model(train_x, test_x, y_train, y_test, iterator):
    grid, y_train, y_test = prepare_grid_regression(y_train, y_test)
    start_time = time.time()
    grid = grid.fit(train_x, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    y_predict = grid.predict(test_x)
    score = grid.best_estimator_.score(test_x, y_predict)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_KNN, iterator)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        Plot.create_measure_table_regression(score, y_predict, y_test, exec_time),
        Rs.MODEL_TYPE_KNN, iterator)


def prepare_grid_regression(train_x):
    Rs.KNN_METRIC_PARAMS.pop('V', numpy.array(numpy.cov(train_x)))
    param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)), weights=Rs.KNN_WEIGHTS,
                      algorithm=Rs.KNN_ALGORITHM, leaf_size=Rs.KNN_LEAF_SIZE, p=Rs.KNN_P_PARAM, metric=Rs.KNN_METRIC
                      )
    grid = GridSearchCV(KNeighborsRegressor(), param_grid, verbose=4, refit=True, cv=Rs.CV)
    return grid


def prepare_grid_classification(y_train, y_test):
    y_train = y_train.replace([0.25, 0.5, 0.75], 1).astype('int')
    y_test = y_test.replace([0.25, 0.5, 0.75], 1).astype('int')
    # todo
    # param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)), weights=Rs.KNN_WEIGHTS,
    #                   algorithm=Rs.KNN_ALGORITHM, leaf_size=Rs.KNN_LEAF_SIZE, p=Rs.KNN_P_PARAM, metric=Rs.KNN_METRIC
    #                   )
    param_grid = {'algorithm': ['auto'], 'leaf_size': [30], 'metric': ['minkowski'], 'metric_params': [None],
                  'n_jobs': [-1],
                  'n_neighbors': [25], 'p': [2], 'weights': ['distance']}

    grid = GridSearchCV(KNeighborsClassifier(), param_grid, verbose=4, refit=True,
                        scoring='accuracy', error_score=0)
    return grid, y_train, y_test

import time

import numpy
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.Elaboration.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" K nearest neighbours algorithm performance """


def create_train_save_model(train_x, test_x, y_train, y_test, iterator):
    # grid = prepare_grid_regresion(train_x)
    grid, y_train, y_test = prepare_grid_classification(y_train, y_test)
    start_time = time.time()
    grid.fit(train_x, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    score = grid.score(test_x, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_KNN, iterator)
    y_predict = grid.predict(test_x)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        Plot.create_measure_table(score, y_predict, y_test, y_train, exec_time),
        Rs.MODEL_TYPE_KNN, iterator)


def prepare_grid_regresion(train_x):
    Rs.KNN_METRIC_PARAMS.pop('V', numpy.array(numpy.cov(train_x)))
    param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)), weights=Rs.KNN_WEIGHTS,
                      algorithm=Rs.KNN_ALGORITHM, leaf_size=Rs.KNN_LEAF_SIZE, p=Rs.KNN_P_PARAM, metric=Rs.KNN_METRIC
                      )
    grid = GridSearchCV(KNeighborsRegressor(), param_grid, verbose=3, refit=True, cv=Rs.CV)
    return grid


def prepare_grid_classification(y_train, y_test):
    y_train = y_train.replace([2, 3, 4], 1).astype('int')
    y_test = y_test.replace([2, 3, 4], 1).astype('int')
    param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)), weights=Rs.KNN_WEIGHTS,
                      algorithm=Rs.KNN_ALGORITHM, leaf_size=Rs.KNN_LEAF_SIZE, p=Rs.KNN_P_PARAM, metric=Rs.KNN_METRIC
                      )
    grid = GridSearchCV(KNeighborsClassifier(), param_grid, verbose=3, refit=True, cv=Rs.CV)
    return grid, y_train, y_test

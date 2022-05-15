import time

import numpy
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" Training algorithm performance """


def train_model(grid, x_train, x_test, y_train, y_test):
    start_time = time.time()
    grid_fitted = grid.fit(x_train, y_train)
    end_time = time.time()
    fit_time = end_time - start_time
    train_accuracy = grid_fitted.score(x_train, y_train)
    start_time = time.time()
    y_predict = grid_fitted.predict(x_test)
    end_time = time.time()
    predict_time = end_time - start_time
    score = grid_fitted.best_score_ * 100

    test_accuracy = grid_fitted.score(x_test, y_test)
    classification_report_result = classification_report(y_test, y_predict)
    measure_table = Plot.create_measure_table(score, y_predict, y_test, fit_time, predict_time,
                                              classification_report_result, train_accuracy, test_accuracy)
    return measure_table, grid_fitted


def save_model(grid_fitted, model_type, iterator, measure_table):
    Ms.save_grid_scores(grid_fitted, model_type, iterator)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        measure_table, model_type, iterator)

import time

import numpy
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" K nearest neighbours algorithm performance """


def train_model(grid, x_train, x_test, y_train, y_test):
    start_time = time.time()
    grid_fitted = grid.fit(x_train, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    y_predict = grid_fitted.predict(x_test)
    score = grid_fitted.best_score_ * 100
    measure_table = Plot.create_measure_table(score, y_predict, y_test, exec_time)
    return measure_table, grid_fitted


def save_model(grid_fitted, model_type, iterator, measure_table):
    Ms.save_grid_scores(grid_fitted, model_type, iterator)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        measure_table, model_type, iterator)

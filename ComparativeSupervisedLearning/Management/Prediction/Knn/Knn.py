import time

import numpy
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms
import ComparativeSupervisedLearning.Management.Prediction.TrainingManager as Tm
import ComparativeSupervisedLearning.Management.Prediction.PredictionManager as Pr
"""" K nearest neighbours algorithm performance """


def create_train_save_model(x_train_, x_test_, y_train_, y_test_, iterator):
    scorer_r_table = dict()
    for scorer, scorer_macro in Rs.SCORER_DICTIONARY.items():
        x_train, x_test, y_train, y_test = Pr.copy_processing_dataset(x_train_, x_test_, y_train_, y_test_)
        grid, y_train, y_test = prepare_grid_classification(y_train, y_test, scoring=scorer_macro)
        measure_table, grid_fitted = Tm.train_model(grid, x_train, x_test, y_train, y_test)
        if scorer == "accuracy":
            Tm.save_model(grid_fitted, Rs.MODEL_TYPE_KNN, iterator, measure_table)
        scorer_r_table.update({scorer: [grid_fitted.cv_results_['split0_test_score'],
                                        grid_fitted.cv_results_['split1_test_score'],
                                        grid_fitted.cv_results_['split2_test_score'],
                                        grid_fitted.cv_results_['split3_test_score']]})
    Ms.save_scorer_models(Rs.MODEL_TYPE_KNN, scorer_r_table)


def create_train_save_regression_model(train_x, test_x, y_train, y_test, iterator):
    grid, y_train, y_test = prepare_grid_regression(y_train, y_test)
    start_time = time.time()
    grid_fitted = grid.fit(train_x, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    y_predict = grid_fitted.predict(test_x)
    score = grid_fitted.best_estimator_.score(test_x, y_predict)
    Ms.save_grid_scores(grid_fitted, Rs.MODEL_TYPE_KNN, iterator)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        Plot.create_measure_table_regression(score, y_predict, y_test, exec_time),
        Rs.MODEL_TYPE_KNN, iterator)


def prepare_grid_regression(train_x):
    Rs.KNN_METRIC_PARAMS.pop('V', numpy.array(numpy.cov(train_x)))
    param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)), weights=Rs.KNN_WEIGHTS,
                      algorithm=Rs.KNN_ALGORITHM, leaf_size=Rs.KNN_LEAF_SIZE, p=Rs.KNN_P_PARAM, metric=Rs.KNN_METRIC
                      )
    grid = GridSearchCV(KNeighborsRegressor(), param_grid, verbose=Rs.VERBOSE, refit=True, cv=Rs.CV)
    return grid


def prepare_grid_classification(y_train, y_test, scoring):
    y_train = y_train.replace([0.25, 0.5, 0.75], 1).astype('int')
    y_test = y_test.replace([0.25, 0.5, 0.75], 1).astype('int')
    param_grid_p = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)), weights=Rs.KNN_WEIGHTS,
                        algorithm=Rs.KNN_ALGORITHM, leaf_size=Rs.KNN_LEAF_SIZE, p=Rs.KNN_P_PARAM, metric=Rs.KNN_METRIC)
    param_grid = {'algorithm': ['auto'], 'leaf_size': [30], 'metric': ['minkowski'], 'metric_params': [None],
                  'n_jobs': [-1],
                  'n_neighbors': [25], 'p': [2], 'weights': ['distance']}
    grid = GridSearchCV(KNeighborsClassifier(), param_grid_p, verbose=Rs.VERBOSE, refit=True,
                        scoring=scoring)
    return grid, y_train, y_test

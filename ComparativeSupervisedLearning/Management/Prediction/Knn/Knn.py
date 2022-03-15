import numpy
import time
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.Elaboration.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" K nearest neighbours algorithm performance """


# todo del
def print_grid_scores(grid):
    print('Parameters')
    print(grid.get_params())

    # Array of 10 accuracy scores during 10-fold cv using the parameters
    print('')
    print('CV Validation Score')
    print(grid.cv)

    # Mean of the 10 scores
    print('')
    print('Mean Validation Score')
    print(grid.cv_results_)

    # create a list of the mean scores only
    # list comprehension to loop through grid.grid_scores
    grid_mean_scores = [result.mean_validation_score for result in grid.score_samples]
    print(grid_mean_scores)

    # examine the best model
    print('Single best score achieved across all params (k)')
    print(grid.best_score_)

    # Dictionary containing the parameters (k) used to generate that score
    print(grid.best_params_)

    # Actual model object fit with those best parameters
    # Shows default parameters that we did not specify
    print(grid.best_estimator_)


# ‘explained_variance’
# ‘max_error’
# ‘neg_mean_absolute_error’
# ‘neg_mean_squared_error’
# ‘neg_root_mean_squared_error’
# ‘neg_mean_squared_log_error’
# ‘neg_median_absolute_error’
# ‘r2’
# ‘neg_mean_poisson_deviance’
# ‘neg_mean_gamma_deviance’
# ‘neg_mean_absolute_percentage_error’

def create_train_save_model(train_x, test_x, y_train, y_test):
    Rs.KNN_METRIC_PARAMS.pop('V', numpy.array(numpy.cov(train_x)))
    param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)), weights=Rs.KNN_WEIGHTS,
                      algorithm=Rs.KNN_ALGORITHM, leaf_size=Rs.KNN_LEAF_SIZE, p=Rs.KNN_P_PARAM, metric=Rs.KNN_METRIC
                      )
    grid = GridSearchCV(KNeighborsRegressor(), param_grid, verbose=3, refit=True, cv=Rs.CV)
    start_time = time.time()
    grid.fit(train_x, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    score = grid.score(test_x, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_KNN)
    y_predict = grid.predict(test_x)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        Plot.create_measure_table(score, y_predict, y_test, y_train, exec_time),
        Rs.MODEL_TYPE_KNN)

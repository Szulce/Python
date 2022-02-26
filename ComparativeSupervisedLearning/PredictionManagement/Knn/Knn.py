from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms


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
    param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)))
    grid = GridSearchCV(KNeighborsRegressor(), param_grid, cv=Rs.KNN_GRID_SPLITER, scoring='max_error', verbose=2)
    grid.fit(train_x, y_train)
    grid.score(test_x, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_KNN)

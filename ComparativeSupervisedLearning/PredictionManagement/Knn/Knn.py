import numpy
import pandas
from sklearn.datasets import load_iris
from sklearn.exceptions import NotFittedError
from sklearn.metrics import mean_squared_error, accuracy_score
import seaborn as sns
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import GridSearchCV, cross_val_score
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier


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


def save_grid_scores(grid):
    pass


# todo generate images ,save imges ,  load images on webside for grid scores
# todo make charts and save compare results fro different imputors

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

def create_train_save_model(data):
    param_grid = dict(n_neighbors=list(range(1, Rs.N_NEIGHBORS_SIZE)))
    grid = GridSearchCV(KNeighborsRegressor(), param_grid, cv=Rs.KNN_GRID_SPLITER, scoring='max_error')
    # grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=Rs.KNN_GRID_SPLITER, scoring='accuracy') todo change y to 01 values
    x = data.iloc[:, :-1]
    y = data.iloc[:, -1:]
    grid.fit(x, y)
    grid.score(x, y)
    # print_grid_scores(grid)
    best_params = grid.best_params_
    best_knn = KNeighborsRegressor(n_neighbors=best_params['n_neighbors'])
    best_knn.fit(x, y)
    Ms.save_model(best_knn, Rs.MODEL_TYPE_KNN + str(1), Rs.MODEL_TYPE_KNN)
    Ms.save_model(grid, Rs.MODEL_TYPE_KNN + str(2), Rs.MODEL_TYPE_KNN)
    save_grid_scores(grid)

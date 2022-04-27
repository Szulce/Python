from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import time
import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.Elaboration.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" Random fores algorithm performance """


def create_train_save_model(x_train, x_test, y_train, y_test, iterator):
    grid = prepare_grid_regression()
    # grid, y_train, y_test = prepare_grid_classification(y_train, y_test)
    start_time = time.time()
    grid.fit(x_train, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    score = grid.score(x_test, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_RF, iterator)
    y_predict = grid.predict(x_test)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        Plot.create_measure_table(score, y_predict, y_test, y_train, exec_time),
        Rs.MODEL_TYPE_RF, iterator)


def prepare_grid_regression():
    param_grid = {'random_state': Rs.RF_RANDOM_STATE, 'max_features': Rs.RF_MAX_FEATURES,
                  'criterion': Rs.RF_CRITERION, 'splitter': Rs.RF_SPLITTER,
                  'min_samples_leaf': Rs.RF_MIN_SAMPLES_LEAF,
                  'min_weight_fraction_leaf': Rs.RF_MIN_WEIGHT_FRACTION_LEAF,
                  'min_impurity_decrease': Rs.RF_MIN_IMPURITY_DECREASE, 'ccp_alpha': Rs.RF_CPP}
    grid = GridSearchCV(DecisionTreeRegressor(), param_grid, refit=True, verbose=3, cv=Rs.CV)
    return grid


def prepare_grid_classification(y_train, y_test):
    y_train = y_train.replace([2, 3, 4], 1).astype('int')
    y_test = y_test.replace([2, 3, 4], 1).astype('int')
    param_grid = {'random_state': Rs.RF_RANDOM_STATE, 'max_features': Rs.RF_MAX_FEATURES,
                  'criterion': Rs.RF_CRITERION, 'splitter': Rs.RF_SPLITTER,
                  'min_samples_leaf': Rs.RF_MIN_SAMPLES_LEAF,
                  'min_weight_fraction_leaf': Rs.RF_MIN_WEIGHT_FRACTION_LEAF,
                  'min_impurity_decrease': Rs.RF_MIN_IMPURITY_DECREASE, 'ccp_alpha': Rs.RF_CPP}
    grid = GridSearchCV(RandomForestClassifier(), param_grid, verbose=3, refit=True, cv=Rs.CV)
    return grid, y_train, y_test

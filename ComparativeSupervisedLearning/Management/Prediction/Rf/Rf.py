from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import GridSearchCV

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms
import ComparativeSupervisedLearning.Management.Prediction.TrainingManager as Tm

"""" Random fores algorithm performance """


def create_train_save_model(x_train, x_test, y_train, y_test, iterator):
    scorer_r_table = dict()
    for scorer, scorer_macro in Rs.SCORER_DICTIONARY.items():
        grid, y_train, y_test = prepare_grid_classification(y_train, y_test, scoring=scorer_macro)
        measure_table, grid_fitted = Tm.train_model(grid, x_train, x_test, y_train, y_test)
        if scorer == 'accuracy':
            Tm.save_model(grid_fitted, Rs.MODEL_TYPE_RF, iterator, measure_table)
        scorer_r_table.update({scorer: [grid_fitted.cv_results_['split0_test_score'],
                                        grid_fitted.cv_results_['split1_test_score'],
                                        grid_fitted.cv_results_['split2_test_score'],
                                        grid_fitted.cv_results_['split3_test_score']]})
    Ms.save_scorer_models(Rs.MODEL_TYPE_RF, scorer_r_table)


def prepare_grid_regression():
    param_grid = {'random_state': Rs.RF_RANDOM_STATE, 'max_features': Rs.RF_MAX_FEATURES,
                  'criterion': Rs.RF_CRITERION, 'splitter': Rs.RF_SPLITTER,
                  'min_samples_leaf': Rs.RF_MIN_SAMPLES_LEAF,
                  'min_weight_fraction_leaf': Rs.RF_MIN_WEIGHT_FRACTION_LEAF,
                  'min_impurity_decrease': Rs.RF_MIN_IMPURITY_DECREASE, 'ccp_alpha': Rs.RF_CPP}
    grid = GridSearchCV(RandomForestRegressor(), param_grid, refit=True, verbose=4, cv=Rs.CV)
    return grid


def prepare_grid_classification(y_train, y_test, scoring):
    y_train = y_train.replace([0.25, 0.5, 0.75], 1).astype('int')
    y_test = y_test.replace([0.25, 0.5, 0.75], 1).astype('int')
    param_grid_p = {'random_state': Rs.RF_RANDOM_STATE, 'max_features': Rs.RF_MAX_FEATURES,
                    'criterion': Rs.RF_CRITERION,
                    'min_samples_leaf': Rs.RF_MIN_SAMPLES_LEAF,
                    'min_weight_fraction_leaf': Rs.RF_MIN_WEIGHT_FRACTION_LEAF,
                    'min_impurity_decrease': Rs.RF_MIN_IMPURITY_DECREASE, 'ccp_alpha': Rs.RF_CPP}
    param_grid = {'random_state': list(range(1, 2))}
    grid = GridSearchCV(RandomForestClassifier(), param_grid, verbose=4, refit=True, cv=Rs.CV, scoring=scoring)
    return grid, y_train, y_test

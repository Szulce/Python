from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR, SVC

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms
import ComparativeSupervisedLearning.Management.Prediction.TrainingManager as Tm
import ComparativeSupervisedLearning.Management.Prediction.PredictionManager as Pr


"""" Support Vector Machines nearest neighbours algorithm performance """


def create_train_save_model(x_train_, x_test_, y_train_, y_test_, iterator):
    scorer_r_table = dict()
    for scorer, scorer_macro in Rs.SCORER_DICTIONARY.items():
        x_train, x_test, y_train, y_test = Pr.copy_processing_dataset(x_train_, x_test_, y_train_, y_test_)
        grid, y_train, y_test = prepare_grid_classification(y_train, y_test, scoring=scorer_macro)
        measure_table, grid_fitted = Tm.train_model(grid, x_train, x_test, y_train, y_test)
        if scorer == 'accuracy':
            Tm.save_model(grid_fitted, Rs.MODEL_TYPE_SVM, iterator, measure_table)
        scorer_r_table.update({scorer: [grid_fitted.cv_results_['split0_test_score'],
                                        grid_fitted.cv_results_['split1_test_score'],
                                        grid_fitted.cv_results_['split2_test_score'],
                                        grid_fitted.cv_results_['split3_test_score']]})
    Ms.save_scorer_models(Rs.MODEL_TYPE_SVM, scorer_r_table)


def prepare_grid_regression():
    param_grid = {'C': Rs.SVM_C, 'gamma': Rs.SVM_GAMMA, 'kernel': Rs.SVM_KERNEL, 'degree': Rs.SVM_DEGREE,
                  'coef0': Rs.SVM_COE0FLOAT, 'epsilon': Rs.SVM_EPSILON, 'shrinking': Rs.SVM_SHRINKING,
                  'cache_size': Rs.SVM_CACHE_SIZE}
    grid = GridSearchCV(SVR(), param_grid, refit=True, verbose=Rs.VERBOSE, cv=Rs.CV)
    return grid


def prepare_grid_classification(y_train, y_test, scoring):
    y_train = y_train.replace([0.25, 0.5, 0.75], 1).astype('int')
    y_test = y_test.replace([0.25, 0.5, 0.75], 1).astype('int')
    param_grid_p = {'C': Rs.SVM_C, 'gamma': Rs.SVM_GAMMA, 'kernel': Rs.SVM_KERNEL, 'degree': Rs.SVM_DEGREE,
                    'coef0': Rs.SVM_COE0FLOAT, 'shrinking': Rs.SVM_SHRINKING,
                    'cache_size': Rs.SVM_CACHE_SIZE}
    param_grid = {'C': list(range(1, 2))}
    grid = GridSearchCV(SVC(), param_grid_p, verbose=Rs.VERBOSE, refit=True, cv=Rs.CV, scoring=scoring)
    return grid, y_train, y_test

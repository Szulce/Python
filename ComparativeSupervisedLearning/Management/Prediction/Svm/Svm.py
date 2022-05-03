from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR, SVC
import time
import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms

"""" Support Vector Machines nearest neighbours algorithm performance """


def create_train_save_model(x_train, x_test, y_train, y_test, iterator):
    grid, y_train, y_test = prepare_grid_classification(y_train, y_test)
    start_time = time.time()
    grid_fitted = grid.fit(x_train, y_train)
    end_time = time.time()
    exec_time = end_time - start_time
    y_predict = grid_fitted.predict(x_test)
    score = grid_fitted.best_score_ * 100
    # print(classification_report(y_test, y_predict))
    Ms.save_grid_scores(grid_fitted, Rs.MODEL_TYPE_SVM, iterator)
    ComparativeSupervisedLearning.Management.Prediction.ModelStorage.save_prediction_to_json(
        Plot.create_measure_table(score, y_predict, y_test, exec_time),
        Rs.MODEL_TYPE_SVM, iterator)


def prepare_grid_regression():
    param_grid = {'C': Rs.SVM_C, 'gamma': Rs.SVM_GAMMA, 'kernel': Rs.SVM_KERNEL, 'degree': Rs.SVM_DEGREE,
                  'coef0': Rs.SVM_COE0FLOAT, 'epsilon': Rs.SVM_EPSILON, 'shrinking': Rs.SVM_SHRINKING,
                  'cache_size': Rs.SVM_CACHE_SIZE}
    grid = GridSearchCV(SVR(), param_grid, refit=True, verbose=4, cv=Rs.CV)
    return grid


def prepare_grid_classification(y_train, y_test):
    y_train = y_train.replace([0.25, 0.5, 0.75], 1).astype('int')
    y_test = y_test.replace([0.25, 0.5, 0.75], 1).astype('int')
    # param_grid = {'C': Rs.SVM_C, 'gamma': Rs.SVM_GAMMA, 'kernel': Rs.SVM_KERNEL, 'degree': Rs.SVM_DEGREE,
    #               'coef0': Rs.SVM_COE0FLOAT, 'shrinking': Rs.SVM_SHRINKING,
    #               'cache_size': Rs.SVM_CACHE_SIZE}
    param_grid = {'C': list(range(1,2))}
    grid = GridSearchCV(SVC(), param_grid, verbose=4, refit=True, cv=Rs.CV)
    return grid, y_train, y_test

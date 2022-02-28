from sklearn.model_selection import GridSearchCV
# training a Decision Tree model
from sklearn.svm import SVR

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.Data.DataConversion as Dc
import ComparativeSupervisedLearning.Management.Elaboration.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms


def create_train_save_model(x_train, x_test, y_train, y_test):
    param_grid = {'C': Rs.SVM_C, 'gamma': Rs.SVM_GAMMA, 'kernel': Rs.SVM_KERNEL}
    grid = GridSearchCV(SVR(), param_grid, refit=True, verbose=2)
    grid.fit(x_train, y_train)
    grid.score(x_test, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_SVM)
    y_predict = grid.predict(x_test)
    Dc.save_prediction_to_json(Plot.create_measure_table(grid.score(x_test, y_test), y_predict, y_test, y_train),
                               Rs.MODEL_TYPE_SVM)

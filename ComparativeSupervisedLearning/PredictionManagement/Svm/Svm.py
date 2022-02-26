from sklearn.model_selection import GridSearchCV
# training a Decision Tree model
from sklearn.svm import SVC, SVR

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms


def create_train_save_model(x_train, x_test, y_train, y_test):
    param_grid = {'C': Rs.SVM_C, 'gamma': Rs.SVM_GAMMA, 'kernel': Rs.SVM_KERNEL}
    grid = GridSearchCV(SVR(), param_grid, refit=True, verbose=2)
    grid.fit(x_train, y_train)
    grid.score(x_test, y_test)
    Ms.save_grid_scores(grid, Rs.MODEL_TYPE_SVM)

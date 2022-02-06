import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import numpy
import pandas
from sklearn.exceptions import NotFittedError
from sklearn.metrics import mean_squared_error
import seaborn as sns
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import GridSearchCV
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
from sklearn.neighbors import KNeighborsRegressor
# training a Decision Tree model
from sklearn.svm import SVR
# measuring RMSE score
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
# measuring RMSE score
from sklearn.metrics import mean_squared_error


def create_train_save_model(x_train, x_test, y_train, y_test):
    iteration = 1
    rmse = []

    # SVR
    svr = SVR(kernel='rbf', C=5)

    rmse = []
    accuracy = []

    # model fitting and measuring RMSE
    for i in range(len(x_train)):
        # fit
        svr.fit(x_train[i], y_train)
        # predict
        pred = svr.predict(x_test[i])
        # RMSE
        rmse.append(numpy.sqrt(mean_squared_error(y_test, pred)))
        # accuracy.append(accuracy_score(y_test, pred) * 100)

    dt_svn = pandas.DataFrame({'RMSE': rmse}, index=['Original', 'Normalized', 'Standardized'])

    Ms.save_model(svr, Rs.MODEL_TYPE_SVN + str(iteration), Rs.MODEL_TYPE_SVN)
    iteration += 1

import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import numpy
import pandas
from sklearn.exceptions import NotFittedError
from sklearn.metrics import mean_squared_error, accuracy_score
import seaborn as sns
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import GridSearchCV
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
from sklearn.neighbors import KNeighborsRegressor
# training a Decision Tree model
from sklearn.tree import DecisionTreeRegressor
# measuring RMSE score
from sklearn.metrics import mean_squared_error


def create_train_save_model(x_train, x_test, y_train, y_test):
    iteration = 1
    rmse = []
    # Decision tree
    dt = DecisionTreeRegressor(max_depth=10, random_state=27)
    # DecisionTreeClassifier(ccp_alpha=0.0, class_weight=None, criterion='gini',
    #                        max_depth=8, max_features=None, max_leaf_nodes=None,
    #                        min_impurity_decrease=0.0, min_impurity_split=None,
    #                        min_samples_leaf=1, min_samples_split=2,
    #                        min_weight_fraction_leaf=0.0, presort='deprecated',
    #                        random_state=None, splitter='best')
    rmse = []
    accuracy = []
    # model fitting and measuring RMSE
    for i in range(len(x_train)):
        # fit
        dt.fit(x_train[i], y_train)
        # predict
        pred = dt.predict(x_test[i])
        # RMSE
        rmse.append(numpy.sqrt(mean_squared_error(y_test, pred)))
        # accuracy.append(accuracy_score(y_test, pred) * 100)
    # visualizing the result
    df_dt = pandas.DataFrame({'RMSE': rmse}, index=['Original', 'Normalized', 'Standardized'])

    Ms.save_model(dt, Rs.MODEL_TYPE_RF + str(iteration), Rs.MODEL_TYPE_RF)
    iteration += 1

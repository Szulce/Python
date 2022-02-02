import numpy
import pandas
from sklearn.metrics import mean_squared_error

import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
from sklearn.neighbors import KNeighborsRegressor


def create_train_save_model(x_train, x_test,y_train,y_test):
    iteration = 1

    # create variants foreach :
    created_model = []  # todo
    # parametry charakterystyczne dla danego modelu
    ## algorytmy wyboru k
    ###

    # knn
    knn = KNeighborsRegressor(n_neighbors=Rs.N_NEIGHBORS)

    rmse = []


    # model fitting and measuring RMSE
    for i in range(len(x_train)):
        # fit
        knn.fit(x_train[i], y_train)
        # predict
        pred = knn.predict(x_train[i])
        # RMSE
        rmse.append(numpy.sqrt(mean_squared_error(y_test, pred)))

    # visualizing the result
    df_knn = pandas.DataFrame({'RMSE': rmse}, index=['Original', 'Normalized', 'Standardized'])
    df_knn
    # train _1

    Ms.save_model(knn, Rs.MODEL_TYPE_KNN + str(iteration), Rs.MODEL_TYPE_KNN)
    iteration += 1

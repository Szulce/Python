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


def create_train_save_model(x_train, x_test, y_train, y_test):
    iteration = 1
    rmse = []
    accuracy = []
    knn = KNeighborsRegressor(n_neighbors=7)
    # model fitting and measuring RMSE
    for i in range(len(x_train)):
        # fit
        knn.fit(x_train[i], y_train)
        # predict
        pred = knn.predict(x_test[i])
        # RMSE
        rmse.append(numpy.sqrt(mean_squared_error(y_test, pred)))
        # accuracy.append(accuracy_score(y_test, pred) * 100)

    # visualizing the result
    df_knn = pandas.DataFrame({'RMSE': rmse}, index=['Original', 'Normalized', 'Standardized'])
    # parameters = {Rs.N_NEIGHBORS: range(1, Rs.N_NEIGHBORS_SIZE)}
    # gridsearch = GridSearchCV(KNeighborsRegressor(), parameters)
    # for i in range(len(x_train)):
    #     gridsearch.fit(x_train[i], y_train)

    # best_k = gridsearch.best_params_[Rs.N_NEIGHBORS]

    # best_knn = KNeighborsRegressor(n_neighbors=best_k)
    # bagging_model = BaggingRegressor(best_knn, n_estimators=100)
    # for i in range(len(x_train)):
        # test_preds_grid = bagging_model.predict(x_train[i])
        # mean = mean_squared_error(y_test, test_preds_grid)

        # best_knn.fit(x_train[i], y_train)
        # prediction = best_knn.predict(x_train[i])
        # print(y_test)
        # print(prediction)
        # mean = mean_squared_error(y_test, prediction)
    #     rmse.append(numpy.sqrt(mean))
    # df_knn = pandas.DataFrame({'RMSE': rmse}, index=['Original', 'Normalized', 'Standardized'])
    # print(df_knn)
    # cmap = sns.cubehelix_palette(as_cmap=True)
    # f, ax = plt.subplots()
    # points = ax.scatter(X_test[:, 0], X_test[:, 1], c=test_preds, s=50, cmap=cmap)
    # f.colorbar(points)
    # plt.show()

    Ms.save_model(knn, Rs.MODEL_TYPE_KNN + str(iteration), Rs.MODEL_TYPE_KNN)
    iteration += 1

import pandas
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.Data.DataConversion as Dc
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms
from ComparativeSupervisedLearning.Data.Dto.Out.AllAlgorithmsResult import AllAlgorithmsResult
from ComparativeSupervisedLearning.Data.Dto.Out.SingleAlgorithmResult import SingleAlgorithmResult
from ComparativeSupervisedLearning.Management.Prediction.Knn import Knn
from ComparativeSupervisedLearning.Management.Prediction.Rf import Rf
from ComparativeSupervisedLearning.Management.Prediction.Svm import Svm
import ComparativeSupervisedLearning.Management.Elaboration.PlotGeneration.PlotGeneration as Plot


def predict_base_data(base_data):
    return predict_based_on_user_input(base_data)


def predict_full_data(full_data):
    # return predict_based_on_user_input(full_data)
    return AllAlgorithmsResult([], [])


def predict_based_on_user_input(data):
    final_results = []
    for model_type in Rs.MODELS:
        final_results.append(run(model_type, data))
    comparison = compare_multiple_results(final_results)
    return AllAlgorithmsResult(final_results, comparison)


def train_algorithms():
    prepared = Dc.prepare_data()
    for data_sample in prepared:
        x_train, x_test, y_train, y_test = split_data_for_learning_process(data_sample)
        for model_type in Rs.MODELS:
            train(model_type, x_train, x_test, y_train, y_test)
    print("END")


def prepare_data_presentation(result, prediction_model, model_type):
    accuracy_score = Ms.load_accuracy_score(prediction_model)
    # plot1 = Plot.plot_knn(model_type, prediction_model, result)
    plot1 = "tutaj wyjres"  # Plot.plot(model_type, prediction_model)#tod
    # plot1 = Plot.plotx()
    # cv_results_
    # score_samples(X)
    # coef_ = clf.best_estimator_.steps[-1][1].coef_
    # coef_ = clf.best_estimator_.steps[0][1].inverse_transform(coef_)
    # plt.close("all")
    # plt.figure(figsize=(7.3, 2.7))
    # plt.subplot(1, 3, 1)
    # plt.imshow(coef, interpolation="nearest", cmap=plt.cm.RdBu_r)
    # plt.title("True weights")
    # plt.subplot(1, 3, 2)
    # plt.imshow(coef_selection_, interpolation="nearest", cmap=plt.cm.RdBu_r)
    # plt.title("Feature Selection")
    # plt.subplot(1, 3, 3)
    # plt.imshow(coef_agglomeration_, interpolation="nearest", cmap=plt.cm.RdBu_r)
    # plt.title("Feature Agglomeration")
    # plt.subplots_adjust(0.04, 0.0, 0.98, 0.94, 0.16, 0.26)
    # plt.show()
    return SingleAlgorithmResult(plot1, accuracy_score, prediction_model, result)


def simple_predict(model, data):
    processed_data = Dc.data_preprocessing(data.to_data_frame(), False)
    prediction = []
    for data_sample in processed_data:
        result = model.best_estimator_.predict(data_sample)
        prediction.append(result)
    return prediction, model


def predict_based_on_model(model, data, model_type):
    result, prediction_model = simple_predict(model, data)
    return prepare_data_presentation(result, prediction_model, model_type)


def compare_multiple_results(results):
    comparison = []
    # KNN SVM
    comparison.append(Plot.create_figure_two_models_text(results[0], results[1], Rs.MODEL_TYPE_KNN, Rs.MODEL_TYPE_SVM))
    comparison.append(Plot.create_figure_two_models(results[0], results[1], Rs.MODEL_TYPE_KNN, Rs.MODEL_TYPE_SVM))
    # KNN RF
    comparison.append(Plot.create_figure_two_models_text(results[0], results[2], Rs.MODEL_TYPE_KNN, Rs.MODEL_TYPE_RF))
    comparison.append(Plot.create_figure_two_models(results[0], results[2], Rs.MODEL_TYPE_KNN, Rs.MODEL_TYPE_RF))
    # SVM RF
    comparison.append(Plot.create_figure_two_models_text(results[1], results[2], Rs.MODEL_TYPE_SVM, Rs.MODEL_TYPE_RF))
    comparison.append(Plot.create_figure_two_models(results[1], results[2], Rs.MODEL_TYPE_SVM, Rs.MODEL_TYPE_RF))
    # ALL
    plot_1, plot_2, ploy_3, ploy_4, ploy_5, tabledata = Plot.create_comparison_plots(results)
    comparison.append(plot_1)
    comparison.append(plot_2)
    comparison.append(ploy_3)
    comparison.append(ploy_4)
    comparison.append(ploy_5)
    return comparison


# model = pandas.DataFrame({'PRED': result_package}, index=['Original', 'Normalized', 'Standardized'])
# scores = [score_lr, score_nb, score_svm, score_knn, score_dt, score_rf, score_xgb, score_nn]
# algorithms = ["Logistic Regression", "Naive Bayes", "Support Vector Machine", "K-Nearest Neighbors",
#               "Decision Tree", "Random Forest", "XGBoost", "Neural Network"]
#
# for i in range(len(algorithms)):
#     print("The accuracy score achieved using " + algorithms[i] + " is: " + str(scores[i]) + " %")
# sns.set(rc={'figure.figsize': (15, 8)})
# plt.xlabel("Algorithms")
# plt.ylabel("Accuracy score")
#
# sns.barplot(algorithms, scores)


def run(model_type, data):
    model = Ms.load_all_models_for_type(model_type)[0]
    return predict_based_on_model(model, data, model_type)


def split_data_for_learning_process(data_sample):
    data_sample = pandas.DataFrame(data_sample)
    x_col = data_sample.iloc[:, :-1]
    y_col = data_sample.iloc[:, -1]
    return train_test_split(x_col, y_col, test_size=Rs.SCIKIT_test_size, random_state=Rs.SCIKIT_random_state)


def train(model_type, train_x, test_x, y_train, y_test):
    if model_type == Rs.MODEL_TYPE_KNN:
        Knn.create_train_save_model(train_x, test_x, y_train, y_test)
    elif model_type == Rs.MODEL_TYPE_SVM:
        Svm.create_train_save_model(train_x, test_x, y_train, y_test)
    elif model_type == Rs.MODEL_TYPE_RF:
        Rf.create_train_save_model(train_x, test_x, y_train, y_test)
    # elif model_type == Rs.MODEL_TYPE_AUTO:
    #     Auto.create_train_save_model(train_x, test_x, y_train, y_test)


def get_data_info():
    data_set = Dc.get_unprepared_data()
    print(data_set.head())
    data_set = data_set.rename(
        columns={"age": "wiek", "sex": "plec", "cp": "bol_w_klatce_piersiowej", "trestbps": "cisnienie_krwi",
                 "fbs": "cukier", "chol": "cholesterol", "num": "wynik"})
    data_set['stan_zdrowia'] = ["zdrowy" if x == 0 else "chory" for x in data_set['wynik']]
    data_set['plec_tekst'] = ['Kobiety' if x == 0 else 'Mężczyźni' for x in data_set['plec']]
    grouped_by_state_for_gender = data_set.groupby(['plec', 'stan_zdrowia'])['plec']
    description = Plot.get_description(data_set)
    exhibit = [Plot.convert_counts_to_html(data_set['stan_zdrowia'].value_counts()),
               Plot.convert_counts_to_html(grouped_by_state_for_gender.count()).replace("plec stan_zdrowia", "")]
    print_hist = data_set.hist(figsize=(16, 20), bins=50, layout=(4, 4), color=['green'])
    for subplot in print_hist:
        for plot in subplot:
            distribution = Plot.convert_plot_to_html(plot.figure)
    return exhibit, Plot.convert_counts_to_html(
        data_set['plec_tekst'].value_counts()), distribution, Plot.get_coleration(data_set), description


def get_algorithm_info():
    final_results = []
    for model_type in Rs.MODELS:
        for loaded_measures in Dc.read_prediction(model_type):
            final_results.append(loaded_measures)
    final_results.append(compare_multiple_results(final_results))
    return final_results

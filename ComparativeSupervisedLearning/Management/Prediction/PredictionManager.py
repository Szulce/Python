import pandas
from sklearn.model_selection import train_test_split

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Data.DataConversion as Dc
import ComparativeSupervisedLearning.Management.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms
from ComparativeSupervisedLearning.Data.Dto.Out.AlgotitmWebInfo import AlgorithmWebInfo
from ComparativeSupervisedLearning.Data.Dto.Out.AllAlgorithmsResult import AllAlgorithmsResult
from ComparativeSupervisedLearning.Data.Dto.Out.DataResultObject import DataResultObject
from ComparativeSupervisedLearning.Data.Dto.Out.SingleAlgorithmResult import SingleAlgorithmResult
from ComparativeSupervisedLearning.Management.Prediction.Knn import Knn
from ComparativeSupervisedLearning.Management.Prediction.Rf import Rf
from ComparativeSupervisedLearning.Management.Prediction.Svm import Svm


def predict_based_on_user_input(data):
    final_results = []
    for model_type in Rs.MODELS:
        final_results.append(run(model_type, data))
    return AllAlgorithmsResult(final_results)


def train_algorithms():
    prepared = Dc.prepare_data()
    iterator = 0
    for data_sample in prepared:
        x_train, x_test, y_train, y_test = split_data_for_learning_process(data_sample)
        for model_type in Rs.MODELS:
            train(model_type, x_train, x_test, y_train, y_test, iterator)
        iterator += 1
    print("END")


def render_data_info():
    exhibit, gender, distribution, coleration, data_info = get_data_info()
    Ms.save_plots(DataResultObject(data_info, exhibit, gender, distribution, coleration).to_json(), Rs.DATA_INFO_PLOTS)


def render_algorithms_info():
    data = get_algorithm_info()
    Ms.save_plots(AlgorithmWebInfo(data).to_json(), Rs.ALGORITHM_INFO_PLOTS)


def prepare_data_presentation(result, prediction_model):
    accuracy_score = Ms.load_accuracy_score(prediction_model)
    plot1 = []
    return SingleAlgorithmResult(plot1, accuracy_score, prediction_model, result)


def simple_predict(model, data):
    processed_data = Dc.data_preprocessing(data.to_data_frame(), False)
    prediction = []
    for data_sample in processed_data:
        result = model.best_estimator_.predict(data_sample)
        prediction.append(result)
    return prediction, model


def predict_based_on_model(model, data):
    result, prediction_model = simple_predict(model, data)
    return prepare_data_presentation(result, prediction_model)


def run(model_type, data):
    model = Ms.load_all_models_for_type(model_type)[0]
    return predict_based_on_model(model, data)


def split_data_for_learning_process(data_sample):
    data_sample = pandas.DataFrame(data_sample)
    x_col = data_sample.iloc[:, :-1]
    y_col = data_sample.iloc[:, -1]
    return train_test_split(x_col, y_col, test_size=Rs.SCIKIT_test_size, random_state=Rs.SCIKIT_random_state)


def train(model_type, train_x_, test_x_, y_train_, y_test_, iterator):
    test_x, train_x, y_test, y_train = copy_processing_dataset(test_x_, train_x_, y_test_, y_train_)
    if model_type == Rs.MODEL_TYPE_KNN:
        Knn.create_train_save_model(train_x, test_x, y_train, y_test, iterator)
    elif model_type == Rs.MODEL_TYPE_SVM:
        Svm.create_train_save_model(train_x, test_x, y_train, y_test, iterator)
    elif model_type == Rs.MODEL_TYPE_RF:
        Rf.create_train_save_model(train_x, test_x, y_train, y_test, iterator)


def copy_processing_dataset(test_x_, train_x_, y_test_, y_train_):
    train_x = train_x_.copy()
    test_x = test_x_.copy()
    y_train = y_train_.copy()
    y_test = y_test_.copy()
    return test_x, train_x, y_test, y_train


def get_data_info():
    data_set = Dc.get_unprepared_data()
    data_set = rename_pl_dataset(data_set)
    grouped_by_state_for_gender = data_set.groupby(['plec', 'stan_zdrowia'])['plec']
    description = Plot.get_description(data_set)
    exhibit = [Plot.convert_counts_to_html(data_set['stan_zdrowia'].value_counts()),
               Plot.convert_counts_to_html(grouped_by_state_for_gender.count()).replace("plec stan_zdrowia", "")]
    print_hist = data_set.hist(figsize=(16, 20), bins=50, layout=(4, 4), color=['green'])
    distribution = prepare_distribution_plt(print_hist)

    return exhibit, Plot.convert_counts_to_html(
        data_set['plec_tekst'].value_counts()), distribution, Plot.get_coleration(data_set), description


def prepare_distribution_plt(print_hist):
    distribution = ""
    for subplot in print_hist:
        for plot in subplot:
            distribution = Plot.convert_plot_to_html(plot.figure)
    return distribution


def rename_pl_dataset(data_set):
    data_set = data_set.rename(columns=Rs.COLUMNS)
    data_set['stan_zdrowia'] = ["zdrowy" if x == 0 else "chory" for x in data_set['wynik']]
    data_set['plec_tekst'] = ['Kobiety' if x == 0 else 'Mężczyźni' for x in data_set['plec']]
    return data_set


def get_algorithm_info():
    final_results = []
    for iterator in range(0, len(Rs.IMPUTERS_LIST)):
        for model_type in Rs.MODELS:
            model_result = []
            for loaded_measures in Ms.read_prediction(model_type, iterator):
                model_result.append(loaded_measures)
            final_results.append(model_result)
            estimators, best_params = Plot.best_estimator_compare(iterator, model_type)
            final_results.append(estimators)
            final_results.append(best_params)
    return final_results

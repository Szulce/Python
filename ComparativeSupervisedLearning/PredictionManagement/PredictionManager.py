import numpy
import pandas

from ComparativeSupervisedLearning.DataManagement.Dto.Result.AllAlgorithmsResult import AllAlgorithmsResult
from ComparativeSupervisedLearning.DataManagement.Dto.Result.SingleAlgorithmResult import SingleAlgorithmResult
from ComparativeSupervisedLearning.PredictionManagement.Auto import Auto
from ComparativeSupervisedLearning.PredictionManagement.Knn import Knn
from ComparativeSupervisedLearning.PredictionManagement.Svn import Svn
from ComparativeSupervisedLearning.PredictionManagement.Rf import Rf
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.DataManagement.DataConversion as Dc
from sklearn.model_selection import train_test_split

# measuring RMSE score
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.preprocessing import MinMaxScaler
# data standardization with  sklearn
from sklearn.preprocessing import StandardScaler


def predict_base_data(base_data):
    return predict(base_data)


def predict_full_data(full_data):
    # return predict(full_data)
    return AllAlgorithmsResult([])


def predict(data):
    final_results = []
    for model_type in Rs.MODELS:
        final_results.append(run(model_type, data))
    return AllAlgorithmsResult(compare_multiple_results(final_results))


def printDataSet(train_x, test_x, y_train, y_test):
    print("x:")
    print(train_x)
    print("x test:")
    print(test_x)
    print("y:")
    print(y_train)
    print("y test:")
    print(y_test)


def train_algorithms():
    prepared = Dc.prepare_data()
    for data_sample in prepared:
        x_train, x_test, y_train, y_test = split_data_for_learning_process(data_sample)
        for model_type in Rs.MODELS:
            train(model_type, x_train, x_test, y_train, y_test, data_sample)
    print("end")


def get_all_result_info_for_model_prediction(result, accuracy_score, prediction_model):
    pass


# todo load data for model to present
# load generated images or charts
# estimate scores and data to present
# prepare reslt


def prepare_data_presentation(result, prediction_model):
    accuracy_score = Ms.load_accuracy_score(prediction_model)
    print("The accuracy score achieved using  is: " + str(accuracy_score) + " %")
    print("The result  is: " + str(result) + " %")
    return get_all_result_info_for_model_prediction(result, accuracy_score, prediction_model)


def simple_predict(model, data):
    processed_data = Dc.data_preprocessing(data.to_data_frame(), False)
    prediction = []
    for data_sample in processed_data:
        result = model.predict(data_sample)
        prediction.append(result)
        # model = pandas.DataFrame({'PRED': result_package}, index=['Original', 'Normalized', 'Standardized'])
    return prediction, model


def predict_based_on_model(model, data):
    result, prediction_model = simple_predict(model, data)
    return prepare_data_presentation(result, prediction_model)


def compare_multiple_results(results):
    # todo comapre algorithm results
    return results


def run(model_type, data):
    model = Ms.load_all_models_for_type(model_type)[0]
    return predict_based_on_model(model, data)

    # models = Ms.load_all_models_for_type(model_type)
    # final_results = []
    # for model in models:
    #     final_results.append(predict_based_on_model(model, data))
    # return compare_multiple_results(final_results)


def split_data_for_learning_process(data_sample):
    data_sample = pandas.DataFrame(data_sample)
    x_col = data_sample.iloc[:, :-1]
    y_col = data_sample.iloc[:, -1]
    return train_test_split(x_col, y_col, test_size=Rs.SCIKIT_test_size, random_state=Rs.SCIKIT_random_state)


def train(model_type, train_x, test_x, y_train, y_test, data_sample):
    if model_type == Rs.MODEL_TYPE_KNN:
        Knn.create_train_save_model(data_sample)
    # elif model_type == Rs.MODEL_TYPE_SVN:
    #     Svn.create_train_save_model(train_x, test_x, y_train, y_test)
    # elif model_type == Rs.MODEL_TYPE_RF:
    #     Rf.create_train_save_model(train_x, test_x, y_train, y_test)
    # elif model_type == Rs.MODEL_TYPE_AUTO:
    #     Auto.create_train_save_model(train_x, test_x, y_train, y_test)


def prediction_data_preprocessing(data_sample):
    data_sample = pandas.DataFrame(data_sample, columns=Rs.features_used)
    data_converted = normalization_user_input(standarization_user_input(data_sample))
    x_cols = data_sample.iloc[:, :-1]
    y_col = data_sample.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(x_cols, y_col, test_size=1)
    return (x_test, x_train, y_test, y_train)

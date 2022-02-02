import numpy
import pandas

from ComparativeSupervisedLearning.DataManagement.Dto.Result.AllAlgorithmsResult import AllAlgorithmsResult
from ComparativeSupervisedLearning.DataManagement.Dto.Result.SingleAlgorithmResult import SingleAlgorithmResult
from ComparativeSupervisedLearning.PredictionManagement.Knn import Knn
from ComparativeSupervisedLearning.PredictionManagement.Svn import Svn
from ComparativeSupervisedLearning.PredictionManagement.Rf import Rf
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import ComparativeSupervisedLearning.DataManagement.DataConversion as Dc
from sklearn.model_selection import train_test_split
# measuring RMSE score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
# data standardization with  sklearn
from sklearn.preprocessing import StandardScaler


def predict_base_data(base_data):
    return predict(base_data)


def predict_full_data(full_data):
    return predict(full_data)


def predict(data):
    result_array = []
    for model_type in Rs.MODELS:
        result_array.append(run(model_type, data))

    return AllAlgorithmsResult(result_array)


def train_algorithms():
    for model_type in Rs.MODELS:
        train(model_type)


def prepare_data_presentation(result):
    return result


def simple_predict(model, data):
    # todo prediction
    return "todo prediction"


def predict_based_on_model(model, data):
    result = simple_predict(model, data)
    return prepare_data_presentation(result)


def compare_multiple_results(results):
    return SingleAlgorithmResult(results)


def run(model_type, data):
    models = Ms.load_all_models_for_type(model_type)
    results = []
    for model in models:
        results.append(predict_based_on_model(model, data))
    return compare_multiple_results(results)


def split_depending_on_method(data_sample, split_method):
    print(data_sample)
    data_sample = pandas.DataFrame(data_sample, columns=Rs.features_used)
    x_cols = data_sample.iloc[:, :-1]
    y_col = data_sample.iloc[:, -1]
    if split_method == Rs.SCIKIT_LEARN:
        return train_test_split(x_cols, y_col, test_size=Rs.SCIKIT_test_size, random_state=Rs.SCIKIT_random_state)
    elif split_method == Rs.PANDAS:
        dataframe_train = data_sample.sample(frac=Rs.PANDAS_frac, random_state=Rs.PANDAS_random_state)
        dataframe_test = data_sample.drop(dataframe_train.index)
        return dataframe_train[x_cols], dataframe_test[x_cols], dataframe_train[y_col], dataframe_test[
            y_col].random.rand()
    elif split_method == Rs.NUMPY:
        mask = numpy.random.rand(len(data_sample)) < Rs.NUMPY_mask
        dataframe_train = data_sample[mask]
        dataframe_test = data_sample[~mask]
        return dataframe_train[x_cols], dataframe_test[x_cols], dataframe_train[y_col], dataframe_test[
            y_col].random.rand()


def train(model_type):
    for data_sample in Dc.prepare_data():
        for split_method in Rs.SPLIT_METHODS:
            x_test, x_train, y_train, y_test = data_preprocessing(data_sample, split_method)
            if model_type == Rs.MODEL_TYPE_KNN:
                Knn.create_train_save_model(x_train, x_test, y_train, y_test)
            elif model_type == Rs.MODEL_TYPE_SVN:
                Svn.create_train_save_model(x_train, x_test, y_train, y_test)
            elif model_type == Rs.MODEL_TYPE_RF:
                Rf.create_train_save_model(x_train, x_test, y_train, y_test)


def data_preprocessing(data_sample, split_method):
    x_train, x_test, y_train, y_test = split_depending_on_method(data_sample, split_method)
    x_test_norm, x_train_norm = normalization(x_test, x_train)
    x_test_stand, x_train_stand = standarization(x_test, x_train)
    train_x = [x_train, x_train_norm, x_train_stand]
    test_x = [x_test, x_test_norm, x_test_stand]
    return train_x, test_x, y_train, y_test


def standarization(x_test, x_train):
    for iterator in ['age', 'trestbps', 'chol', 'restecg', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']:
        scale = StandardScaler().fit(x_train[[iterator]])
        x_train[iterator] = scale.transform(x_train[[iterator]])
        x_test[iterator] = scale.transform(x_test[[iterator]])
    return x_test, x_train


def normalization(x_test, x_train):
    norm = MinMaxScaler().fit(x_train)
    return norm.transform(x_test), norm.transform(x_test)

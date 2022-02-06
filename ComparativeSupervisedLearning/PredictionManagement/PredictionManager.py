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
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.preprocessing import MinMaxScaler
# data standardization with  sklearn
from sklearn.preprocessing import StandardScaler


def predict_base_data(base_data):
    return predict(base_data)


def predict_full_data(full_data):
    # return predict(full_data)
    return AllAlgorithmsResult([], [])


def predict(data):
     result_array = []
    scores_array = []
    for model_type in Rs.MODELS:
        result, scores = run(model_type, data)
        result_array.append(result)
        scores_array.append(scores)
    return AllAlgorithmsResult(result_array, scores_array)


def train_algorithms():
    for model_type in Rs.MODELS:
        train(model_type)


def prepare_data_presentation(result, model_pre, score):
    print("The accuracy score achieved using  is: " + str(score[0]) + " %")
    print("The result  is: " + str(result[0]) + " %")
    return result, score


def simple_predict(model, data):
    samples, validation = user_data_preprocessing(data)
    # samples = [[[x_train, x_train_norm, x_train_stand], [x_trst, x_test_norm, x_test_stand], y_train, y_test],
    # [train_x, test_x, y_train, y_test]]
    # xtrain =
    result_package = []
    score = []
    prepared_sample = samples
    # for prepared_sample in samples:
    x = numpy.asarray(prepared_sample[0][0][0])
    y = numpy.asarray(prepared_sample[0][2])
    x_v = numpy.asarray(prepared_sample[0][0][1])
    # y_v = numpy.asarray(prepared_sample[0][3])
    model.fit(x, y)
    prediction_result = model.predict(x_v)
    prediction_result_x = model.predict(x)
    result_package.append(prediction_result)
    score.append(numpy.sqrt(mean_squared_error(y, prediction_result_x)))
    # el_score = round(accuracy_score(y, prediction_result) * 100, 2)
    # score.append(el_score)
    # print("The accuracy score achieved is: " + str(el_score) + " %")
    # for index in range(len(prepared_sample)):
    #     # fit
    #     x = numpy.asarray(prepared_sample[index][0])
    #     y = numpy.asarray(prepared_sample[2])
    #     x_v = numpy.asarray(prepared_sample[index][1])
    #     y_v = numpy.asarray(prepared_sample[3])
    #     model.fit(x, y)
    #     result_package.append(model.predict(x_v))
    #     # el_score = round(accuracy_score(y_v, x_v.reshape(1, -1)) * 100, 2)
    #     # score.append(el_score)
    #     # print("The accuracy score achieved is: " + str(el_score) + " %")
    model = pandas.DataFrame({'PRED': result_package}, index=['Original', 'Normalized', 'Standardized'])
    return result_package, model, score


def predict_based_on_model(model, data):
    result, model_pre, score = simple_predict(model, data)
    return prepare_data_presentation(result, model_pre, score)


def compare_multiple_results(results, score):
    return results, score


def run(model_type, data):
    models = Ms.load_all_models_for_type(model_type)
    results = []
    scores = []
    for model in models:
        result, score = predict_based_on_model(model, data)
        results.append(result)
        scores.append(score)
    return compare_multiple_results(results, scores)


def split_depending_on_method(data_sample, split_method):
    data_sample = pandas.DataFrame(data_sample, columns=Rs.features_used)
    x_cols = data_sample.iloc[:, :-1]
    y_col = data_sample.iloc[:, -1]
    # if split_method == Rs.SCIKIT_LEARN or split_method == Rs.PANDAS:
    return train_test_split(x_cols, y_col, test_size=Rs.SCIKIT_test_size, random_state=Rs.SCIKIT_random_state)
    # elif split_method == Rs.PANDAS:
    #     dataframe_train = data_sample.sample(frac=Rs.PANDAS_frac, random_state=Rs.PANDAS_random_state)
    #     dataframe_test = data_sample.drop(dataframe_train.index)
    #     return dataframe_train[x_cols], dataframe_test[x_cols], dataframe_train[y_col], dataframe_test[
    #         y_col]
    # elif split_method == Rs.NUMPY:
    #     mask = numpy.random.rand(len(data_sample)) < Rs.NUMPY_mask
    #     dataframe_train = data_sample[mask]
    #     dataframe_test = data_sample[~mask]
    #     return dataframe_train[x_cols], dataframe_test[x_cols], dataframe_train[y_col], dataframe_test[
    #         y_col].random.rand()


def train(model_type):
    for data_sample in Dc.prepare_data():
        for split_method in Rs.SPLIT_METHODS:
            train_x, test_x, y_train, y_test = data_preprocessing(data_sample, split_method)
            if model_type == Rs.MODEL_TYPE_KNN:
                Knn.create_train_save_model(train_x, test_x, y_train, y_test)
            elif model_type == Rs.MODEL_TYPE_SVN:
                Svn.create_train_save_model(train_x, test_x, y_train, y_test)
            elif model_type == Rs.MODEL_TYPE_RF:
                Rf.create_train_save_model(train_x, test_x, y_train, y_test)


def user_data_preprocessing(data_sample):
    user_input = data_sample.to_data_frame()
    samples = []
    for data_sample in Dc.prepare_user_input_data(user_input):
        # data_frame = pandas.DataFrame(data_sample[0].reshape(1, -1), columns=Rs.features_used)
        train_x, test_x, y_train, y_test = prediction_data_preprocessing(data_sample)
        samples.append([train_x, test_x, y_train, y_test])
    return samples, Dc.handling_null_values(user_input)


def data_preprocessing(data_sample, split_method):
    x_train, x_test, y_train, y_test = split_depending_on_method(data_sample, split_method)
    return data_prepare(x_test, x_train, y_test, y_train)


def prediction_data_preprocessing(data_sample):
    data_sample = pandas.DataFrame(data_sample, columns=Rs.features_used)
    x_cols = data_sample.iloc[:, :-1]
    y_col = data_sample.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(x_cols, y_col, test_size=1)
    return data_prepare(x_test, x_train, y_test, y_train)


def user_input_data_preprocessing(data_sample):
    norm = normalization_user_input(data_sample)
    stand = standarization_user_input(data_sample)
    return [data_sample, norm, stand]


def data_prepare(x_test, x_train, y_test, y_train):
    x_test_norm, x_train_norm = normalization(x_test, x_train)
    x_test_stand, x_train_stand = standarization(x_test, x_train)
    train_x = [x_train, x_train_norm, x_train_stand]
    test_x = [x_test, x_test_norm, x_test_stand]
    return train_x, test_x, y_train, y_test


def standarization(x_test, x_train):
    temp_x_train = x_train.loc[:, :].copy()
    temp_x_test = x_test.loc[:, :].copy()
    for iterator in ['age', 'trestbps', 'chol', 'restecg', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']:
        scale = StandardScaler().fit(x_train[[iterator]])
        temp_x_train[iterator] = scale.transform(x_train[[iterator]])
        temp_x_test[iterator] = scale.transform(x_test[[iterator]])

    return temp_x_test, temp_x_train


def standarization_user_input(data):
    for iterator in ['age', 'trestbps', 'chol', 'restecg', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']:
        scale = StandardScaler().fit(data[[iterator]])
        data[iterator] = scale.transform(data[[iterator]])
    return data
    # dataset = pandas.DataFrame(data, columns=Rs.features_used)
    # for iterator in ['age', 'trestbps', 'chol', 'restecg', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']:
    #     print(dataset)
    #     print(dataset[[iterator]].reshape(1, -1))
    #     scale = StandardScaler().fit(dataset[[iterator]].reshape(1, -1))
    #     dataset[iterator] = scale.transform(dataset[[iterator]])
    # return dataset


# standardised = []
# for dataset in data:
#     for iterator in ['age', 'trestbps', 'chol', 'restecg', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']:
#         print(dataset)
#         scale = StandardScaler().fit(dataset[[iterator]])
#         dataset[iterator] = scale.transform(dataset[[iterator]])
#     standardised.append(dataset)
# return standardised


def normalization(x_test, x_train):
    norm = MinMaxScaler().fit(x_train)
    print(norm.transform(x_train))
    return norm.transform(x_test), norm.transform(x_train)


def normalization_user_input(data):
    norm = MinMaxScaler().fit(data)
    print(norm.transform(data))
    return norm.transform(data)

    # normalised = []
    # for dataset in data:
    # data_frame = pandas.DataFrame(data[0].reshape(1, -1), columns=Rs.features_used)
    # print(data_frame)
    # norm = MinMaxScaler().fit(data_frame)
    # print(norm.transform(data_frame))
    # return norm.transform(data_frame)
    #   normalised.append(norm.transform(data_frame))
    # print(normalised)
    # return normalised

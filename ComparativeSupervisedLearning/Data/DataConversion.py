import json

from numpy import nanmean
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

from ComparativeSupervisedLearning.Config.LogConfig import mainLogger as Log
import pandas

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs


def load_data_from_files():
    data_directory_path = '../Data/'
    data_files = ['processed.cleveland.data', 'processed.hungarian.data', 'processed.switzerland.data',
                  'processed.va.data']
    load_files = []

    for filename in data_files:
        data_from_file = pandas.read_csv(data_directory_path + filename, sep=',', index_col=None, header=None,
                                         names=Rs.features_used, keep_default_na=False, na_values='?')
        load_files.append(data_from_file)
    return load_files


# data_frame.PlotGeneration(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
# plot_view.show()

# data_frame = data_frame.reshape(920, 14)
# print(data_frame)
# print(data_frame.shape)
# print(data_frame.describe())

# scatter_matrix(data_frame)
# plot_view.show()
def concat_data(load_files):
    data_frame = pandas.concat(load_files, axis=0, ignore_index=True)
    return pandas.DataFrame(data_frame, columns=Rs.features_used)


def handling_null_values(data_frame):
    data_array = []
    for imputed in Rs.IMPUTERS_LIST:
        data_array.append(imputed.fit_transform(data_frame))
    return data_array


def handling_categorical_variables(data, training):
    handled = []
    columns = Rs.features_prediction
    if training:
        columns = Rs.features_used
    for data_set in data:
        data_frame = pandas.DataFrame(data_set, columns=columns)
        data_frame.reindex(Rs.features_used, axis=1)
        handled.append(pandas.get_dummies(data=data_frame, drop_first=training))
    return handled


def normalization(data):
    scaled_array = []
    for data_iter in data:
        scaled = preprocessing.MinMaxScaler().fit_transform(data_iter.values)
        scaled_array.append(pandas.DataFrame(scaled))
    return scaled_array


def standarization(data, training):
    strand_array = []
    columns = Rs.features_prediction
    if training:
        columns = Rs.features_used
    for data_iter in data:
        temp = pandas.DataFrame(data_iter, columns=columns)
        for iterator in Rs.features_used_numerical:
            StandardScaler().fit_transform(temp[[iterator]])
        strand_array.append(data_iter)

    return strand_array


def prepare_data():
    unprepared_data = get_unprepared_data()
    return data_preprocessing(unprepared_data, True)


def get_unprepared_data():
    return concat_data(load_data_from_files())


def data_preprocessing(unprepared_data, training):
    unprepared_data.drop_duplicates(keep='first')
    return normalization(
        handling_categorical_variables(
            standarization(
                handling_null_values(unprepared_data), training), training))


def save_prediction_to_json(prediction, algorithm):
    if algorithm == 'AUTO':
        with open('In/JsonResult/Auto.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'TREE':
        with open('In/JsonResult/Tree.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'SVM':
        with open('In/JsonResult/Svm.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'KNN':
        with open('In/JsonResult/Knn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()


def save_prediction(prediction, algorithm):
    if algorithm == 'AUTO':
        with open('In/JsonResult/Auto.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'TREE':
        with open('In/JsonResult/Tree.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'SVM':
        with open('In/JsonResult/Svm.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'KNN':
        with open('In/JsonResult/Knn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()


def read_prediction(algorithm):
    all_predictions = []
    if algorithm == 'AUTO' or algorithm == 'ALL':
        with open('In/JsonResult/Auto.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'TREE' or algorithm == 'ALL':
        with open('In/JsonResult/Tree.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'SVM' or algorithm == 'ALL':
        with open('In/JsonResult/Svm.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'KNN' or algorithm == 'ALL':
        with open('In/JsonResult/Knn.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    return all_predictions

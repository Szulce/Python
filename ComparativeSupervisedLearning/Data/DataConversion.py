import pandas
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

import ComparativeSupervisedLearning.Config.StaticResources as Rs

"""" Load data for learning proces and preprocess data information """


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



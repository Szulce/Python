import json
from ComparativeSupervisedLearning.Config.LogConfig import mainLogger as Log
import pandas

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs


def load_data_from_files():
    data_directory_path = '../Data/'
    data_files = ['processed.cleveland.Data', 'processed.hungarian.Data', 'processed.switzerland.Data',
                  'processed.va.Data']
    load_files = []

    for filename in data_files:
        data_from_file = pandas.read_csv(data_directory_path + filename, sep=',', index_col=None, header=None,
                                         names=Rs.features_used, keep_default_na=False, na_values='?')
        load_files.append(data_from_file)
    return load_files


# data_frame.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
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
        imputed.fit(data_frame)
        handled = imputed.transform(data_frame)
        # print(handled)
        if list(handled[0]).count('missing_value') > 0:
            for index in range(len(handled[0])):
                if handled[0][index] == 'missing_value':
                    handled[0][index] = -1
        data_array.append(handled)
    # print(data_array)
    return data_array


def handling_categorical_variables(data):
    slices = pandas.Series(data[::])
    return pandas.get_dummies(slices)


def encoding_o_h(data):
    # not necessary but if used  drop first
    # print(data)
    return data


def prepare_data():
    unprepared_data = concat_data(load_data_from_files())
    return encoding_o_h(handling_null_values(unprepared_data))


def prepare_user_input_data(input):
    loaded_files = load_data_from_files()
    loaded_files.append(input)
    unprepared_data = concat_data(loaded_files)
    return encoding_o_h(handling_null_values(unprepared_data))


def save_prediction_to_json(prediction, algorithm):
    if algorithm == 'AUTO':
        with open('DataManagement/JsonResult/Auto.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'TREE':
        with open('DataManagement/JsonResult/Tree.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'SVM':
        with open('DataManagement/JsonResult/Svn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'KNN':
        with open('DataManagement/JsonResult/Knn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()


def save_prediction(prediction, algorithm):
    if algorithm == 'AUTO':
        with open('DataManagement/JsonResult/Auto.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'TREE':
        with open('DataManagement/JsonResult/Tree.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'SVM':
        with open('DataManagement/JsonResult/Svn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == 'KNN':
        with open('DataManagement/JsonResult/Knn.json', 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()


def read_prediction(algorithm):
    all_predictions = []
    if algorithm == 'AUTO' or algorithm == 'ALL':
        with open('DataManagement/JsonResult/Auto.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'TREE' or algorithm == 'ALL':
        with open('DataManagement/JsonResult/Tree.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'SVM' or algorithm == 'ALL':
        with open('DataManagement/JsonResult/Svn.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    if algorithm == 'KNN' or algorithm == 'ALL':
        with open('DataManagement/JsonResult/Knn.json', 'r') as json_f:
            prediction = json.load(json_f)
            for p in prediction:
                all_predictions.append(p)
        json_f.close()
    return all_predictions

import json
import os
import joblib
from ComparativeSupervisedLearning.Config import StaticResources as Rs
from ComparativeSupervisedLearning.Config.LogConfig import mainLogger as Log


def save_model(model, name, model_type):
    filename = os.getcwd() + Rs.PREDICTION_MANAGEMENT_ + model_type + Rs.SAV_DIR + name + '.sav'
    joblib.dump(model, filename)


def save_plots(plots_object, name):
    filename = os.getcwd() + Rs.PREDICTION_ELABORATION_ + name + '.sav'
    joblib.dump(plots_object, filename)


def load_plot_object(name):
    filename = os.getcwd() + Rs.PREDICTION_ELABORATION_ + name + '.sav'
    loaded_object = joblib.load(filename)
    return loaded_object


def load_model(name, model_type):
    filename = os.getcwd() + Rs.PREDICTION_MANAGEMENT_ + model_type + Rs.SAV_DIR + name + '.sav'
    loaded_model = joblib.load(filename)
    Log.debug("Loaded Model " + name)
    return loaded_model


def load_best_models_for_each_algorithm():
    loaded_model_knn = joblib.load(Rs.KNN_FULL_PATH_SAV)
    loaded_model_svn = joblib.load(Rs.SVN_FULL_PATH_SAV)
    loaded_model_rf = joblib.load(Rs.RF_FULL_PATH_SAV)
    Log.debug("Loaded Models")
    return [loaded_model_knn, loaded_model_svn, loaded_model_rf]


def load_all_models_for_type(model_type):
    loaded_models = []
    path = os.getcwd() + Rs.PREDICTION_MANAGEMENT_ + model_type + Rs.SAV_DIR
    for filename in os.listdir(path):
        next_model = joblib.load(str(path) + Rs.SLASH + str(filename))
        loaded_models.append(next_model)
    Log.debug("Loaded Models count:" + str(len(loaded_models)))
    return loaded_models


def load_accuracy_score(prediction_model):
    return prediction_model


def save_grid_scores(grid, model_type, iterator):
    save_model(grid, model_type + str(iterator), model_type)


def load_grid_scores(model_type, iterator):
    return load_model(model_type + str(iterator), model_type)


def save_prediction_to_json(prediction, algorithm, iterator):
    iterator += 1
    if algorithm == Rs.MODEL_TYPE_RF:
        with open('%sTree%s.json' % (Rs.OUT_JSON_RESULT_, str(iterator)), 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == Rs.MODEL_TYPE_SVM:
        with open('%sSvm%s.json' % (Rs.OUT_JSON_RESULT_, str(iterator)), 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()
    elif algorithm == Rs.MODEL_TYPE_KNN:
        with open('%sKnn%s.json' % (Rs.OUT_JSON_RESULT_, str(iterator)), 'w') as json_f:
            json.dump(prediction, json_f)
        json_f.close()


def read_prediction(algorithm, iterator):
    iterator += 1
    all_predictions = []
    if algorithm == Rs.MODEL_TYPE_RF or algorithm == 'ALL':
        with open('%sTree%s.json' % (Rs.OUT_JSON_RESULT_, str(iterator)), 'r') as json_f:
            prediction = json.load(json_f)
            all_predictions.append(prediction)
        json_f.close()
    if algorithm == Rs.MODEL_TYPE_SVM or algorithm == 'ALL':
        with open('%sSvm%s.json' % (Rs.OUT_JSON_RESULT_, str(iterator)), 'r') as json_f:
            prediction = json.load(json_f)
            all_predictions.append(prediction)
        json_f.close()
    if algorithm == Rs.MODEL_TYPE_KNN or algorithm == 'ALL':
        with open('%sKnn%s.json' % (Rs.OUT_JSON_RESULT_, str(iterator)), 'r') as json_f:
            prediction = json.load(json_f)
            all_predictions.append(prediction)
        json_f.close()
    return all_predictions


def load_scorer_models(type_m):
    filename = os.getcwd() + Rs.PREDICTION_ELABORATION_ + type_m + Rs.SCORER_MODEL + '.sav'
    loaded_object = joblib.load(filename)
    return loaded_object


def save_scorer_models(type_m, model_object):
    filename = os.getcwd() + Rs.PREDICTION_ELABORATION_ + type_m + Rs.SCORER_MODEL + '.sav'
    joblib.dump(model_object, filename)

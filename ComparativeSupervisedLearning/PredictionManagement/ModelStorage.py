from ComparativeSupervisedLearning.Config.LogConfig import mainLogger as Log
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import joblib
import os


def save_model(model, name):
    filename = name + '.sav'
    joblib.dump(model, filename)


def load_model(name):
    loaded_model = joblib.load(name)
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
    for filename in os.listdir(Rs.MODULE_DIRECTORY_PATH + model_type + Rs.SAV_DIR):
        next_model = joblib.load(filename)
        loaded_models.append(next_model)
    Log.debug("Loaded Models count:")
    Log.debug(len(loaded_models))
    return loaded_models

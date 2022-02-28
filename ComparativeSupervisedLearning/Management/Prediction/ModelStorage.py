from ComparativeSupervisedLearning.Config.LogConfig import mainLogger as Log
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import joblib
import os


def save_model(model, name, model_type):
    filename = os.getcwd() + Rs.PREDICTION_MANAGEMENT_ + model_type + Rs.SAV_DIR + name + '.sav'
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
    path = os.getcwd() + Rs.PREDICTION_MANAGEMENT_ + model_type + Rs.SAV_DIR
    for filename in os.listdir(path):
        next_model = joblib.load(str(path) + Rs.SLESH + str(filename))
        loaded_models.append(next_model)
    Log.debug("Loaded Models count:" + str(len(loaded_models)))
    return loaded_models


def load_accuracy_score(prediction_model):
    return prediction_model


def save_grid_scores(grid, model_type):
    save_model(grid, model_type + str(1), model_type)

    #save best params   best_params = grid.best_params_
# todo generate images ,save imgaes ,  load images on webside for grid scores
# todo make charts and save compare results fro different imputors

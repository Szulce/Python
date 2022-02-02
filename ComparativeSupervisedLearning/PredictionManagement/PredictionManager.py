from ComparativeSupervisedLearning.DataManagement.Dto.Result.AllAlgorithmsResult import AllAlgorithmsResult
from ComparativeSupervisedLearning.DataManagement.Dto.Result.SingleAlgorithmResult import SingleAlgorithmResult
from ComparativeSupervisedLearning.PredictionManagement.Knn import Knn
from ComparativeSupervisedLearning.PredictionManagement.Svn import Svn
from ComparativeSupervisedLearning.PredictionManagement.Rf import Rf
import ComparativeSupervisedLearning.PredictionManagement.ModelStorage as Ms
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs


def predict_base_data(base_data):
    return predict(base_data)


def predict_full_data(full_data):
    return predict(full_data)


def predict(data):
    # todo prediction
    # todo percentage na true false
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


def train(model_type):
    # create models
    if model_type == Rs.MODEL_TYPE_KNN:
        Knn.create_train_save_model()
    elif model_type == Rs.MODEL_TYPE_SVN:
        Svn.create_train_save_model()
    elif model_type == Rs.MODEL_TYPE_RF:



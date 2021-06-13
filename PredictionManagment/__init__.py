from DataManagement.Dto.Result.AllAlgorithmsResult import AllAlgorithmsResult
from DataManagement.Dto.Result.SingleAlgorithmResult import SingleAlgorithmResult


def predictBaseData(base_data):
    return predict(base_data)


def predictFullData(full_data):
    return predict(full_data)


def predict(data):
    # todo prediction
    result_knn = "50%"
    result_svm = "60%"
    result_rf = "55%"
    return AllAlgorithmsResult(SingleAlgorithmResult(result_knn),
                               SingleAlgorithmResult(result_svm),
                               SingleAlgorithmResult(result_rf))

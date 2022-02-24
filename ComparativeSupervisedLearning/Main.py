from ComparativeSupervisedLearning.PredictionManagement import PredictionManager
from ComparativeSupervisedLearning.PredictionManagement import AutoModel as Au
from ComparativeSupervisedLearning.DataManagement.Dto.Result.FullResultObject import FullResultObject


def predict_based_on_user_input(base_data, full_data):
    base_result = PredictionManager.predict_base_data(base_data)
    full_result = PredictionManager.predict_full_data(full_data)
    return FullResultObject(base_result, full_result, full_data.applyFullResult).to_json()


if __name__ == '__main__':
    PredictionManager.train_algorithms()

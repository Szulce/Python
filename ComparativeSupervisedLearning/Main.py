from ComparativeSupervisedLearning.Data.Dto.Out.DataResultObject import DataResultObject
from ComparativeSupervisedLearning.Data.Dto.Out.FullResultObject import FullResultObject
from ComparativeSupervisedLearning.Management.Prediction import PredictionManager


def predict_based_on_user_input(base_data, full_data):
    base_result = PredictionManager.predict_base_data(base_data)
    full_result = PredictionManager.predict_full_data(full_data)
    return FullResultObject(base_result, full_result, full_data.applyFullResult).to_json()


def render_data_info():
    exhibit, gender, distribution, coleration, data_info = PredictionManager.get_data_info()
    return DataResultObject(data_info, exhibit, gender, distribution, coleration).to_json()


if __name__ == '__main__':
    PredictionManager.train_algorithms()

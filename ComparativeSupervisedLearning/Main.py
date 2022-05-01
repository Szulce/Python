import sys

import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms
from ComparativeSupervisedLearning.Data.Dto.Out.AlgotitmWebInfo import AlgorithmWebInfo
from ComparativeSupervisedLearning.Data.Dto.Out.DataResultObject import DataResultObject
from ComparativeSupervisedLearning.Data.Dto.Out.FullResultObject import FullResultObject
from ComparativeSupervisedLearning.Management.Prediction import PredictionManager

"""" Manages main functions  """


def predict_based_on_user_input(base_data):
    base_result = PredictionManager.predict_based_on_user_input(base_data)
    user_data_plot = Plot.generate_user_data_plot(base_data)
    return FullResultObject(base_result, user_data_plot).to_json()


def get_data_info_object():
    exhibit, gender, distribution, coleration, data_info = PredictionManager.get_data_info()
    return DataResultObject(data_info, exhibit, gender, distribution, coleration).to_json()
    # return Ms.load_plot_object(Rs.DATA_INFO_PLOTS)


def get_algorithms_info_object():
    data = PredictionManager.get_algorithm_info()
    return AlgorithmWebInfo(data).to_json()
    # return Ms.load_plot_object(Rs.ALGORITHM_INFO_PLOTS)


if __name__ == '__main__':
    sys.stdout = open(Rs.LOG_FILES_DIRECTORY + "/" + Rs.LOG_FILE_NAME, 'w')
    PredictionManager.train_algorithms()
    PredictionManager.render_data_info()
    PredictionManager.render_algorithms_info()
    sys.stdout.close()

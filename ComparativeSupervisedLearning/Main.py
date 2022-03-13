import ComparativeSupervisedLearning.Config.StaticResources as Rs
import ComparativeSupervisedLearning.Management.Elaboration.PlotGeneration.PlotGeneration as Plot
import ComparativeSupervisedLearning.Management.Prediction.ModelStorage as Ms
from ComparativeSupervisedLearning.Data.Dto.Out.FullResultObject import FullResultObject
from ComparativeSupervisedLearning.Management.Prediction import PredictionManager

"""" Manages main functions  """


def predict_based_on_user_input(base_data):
    base_result = PredictionManager.predict_based_on_user_input(base_data)
    user_data_plot = Plot.generate_user_data_plot(base_data)
    return FullResultObject(base_result, user_data_plot).to_json()


def get_data_info_object():
    Ms.load_plot_object(Rs.DATA_INFO_PLOTS)


def get_algorithms_info_object():
    Ms.load_plot_object(Rs.ALGORITHM_INFO_PLOTS)


if __name__ == '__main__':
    PredictionManager.train_algorithms()
    PredictionManager.render_data_info()
    PredictionManager.render_algorithms_info()

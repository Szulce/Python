import json


class FullResultObject:
    """"Class defines of object to return results in json format prepared for page  """

    def __init__(self, results_base, user_data_plot):
        self.results_base_positive_negative = get_final_answer(results_base)

        self.results_base_information_text_knn = get_result_as_text(results_base.knn_results.best_result.result)
        self.results_base_information_text_svm = get_result_as_text(results_base.svm_results.best_result.result)
        self.results_base_information_text_rf = get_result_as_text(results_base.rf_results.best_result.result)
        self.results_base_accuracy_text_knn = str(abs(results_base.knn_results.score * 100)) + "%"
        self.results_base_accuracy_text_svm = str(abs(results_base.svm_results.score * 100)) + "%"
        self.results_base_accuracy_text_rf = str(abs(results_base.rf_results.score * 100)) + "%"

        self.results_base_knn_plot = results_base.knn_results.plot1
        self.results_base_svm_plot = results_base.svm_results.plot1
        self.results_base_rf_plot = results_base.rf_results.plot1

        self.user_data_plot1 = user_data_plot[0]
        self.user_data_plot2 = user_data_plot[1]
        self.user_data_plot3 = user_data_plot[2]
        self.user_data_plot4 = user_data_plot[3]
        self.user_data_plot5 = user_data_plot[4]
        self.user_data_plot6 = user_data_plot[5]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


def get_final_answer(results_base):
    answer = False
    for result_iter in results_base.knn_results.result:
        if result_iter < 1:
            answer = True
    for result_iter in results_base.svm_results.result:
        if result_iter < 1:
            answer = True
    for result_iter in results_base.rf_results.result:
        if result_iter < 1:
            answer = True
    return answer


def get_result_as_text(best_result):
    if best_result[0] < 1.0:
        return "Pozytywny (wynik:" + str(best_result[0]) + ")"
    else:
        return "Negatywny (wynik:" + str(best_result[0]) + ")"

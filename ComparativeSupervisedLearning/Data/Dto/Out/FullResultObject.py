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

        self.user_data_plot = user_data_plot
        # czułość
        # self.results_base_knn_result = str(abs(results_base.knn_results.score * 100)) + "%"
        # self.results_base_svm_result = str(abs(results_base.knn_results.score * 100)) + "%"
        # self.results_base_rf_result  = str(abs(results_base.knn_results.score * 100)) + "%"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
        # return jsonpickle.encode(self)


# self.base_result = results_base
# if apply_full:
#     self.full_result = full_result
# else:
#     self.full_result = None
# knn
#        self.results_base_knn_results_plot1 = results_base.knn_results.plot1
#        self.results_base_knn_results_score = results_base.knn_results.score
#        self.results_base_knn_results_result = results_base.knn_results.result
#        self.results_base_knn_results_best_params = results_base.knn_results.best_params
#        self.results_base_knn_results_accuracy_score = results_base.knn_results.accuracy_score
#        # svm
#        self.results_base_svm_results_plot1 = results_base.svm_results.plot1
#        self.results_base_svm_results_score = results_base.svm_results.score
#        self.results_base_svm_results_result = results_base.svm_results.result
#        self.results_base_svm_results_best_params = results_base.svm_results.best_params
#        self.results_base_svm_results_accuracy_score = results_base.svm_results.accuracy_score
#        # rf
#        self.results_base_rf_results_plot1 = results_base.rf_results.plot1
#        self.results_base_rf_results_score = results_base.rf_results.score
#        self.results_base_rf_results_result = results_base.rf_results.result
#        self.results_base_rf_results_best_params = results_base.rf_results.best_params
#        self.results_base_rf_results_accuracy_score = results_base.rf_results.accuracy_score
#        # comparation
#        self.base_result_comparison_results = results_base.comparison_results

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

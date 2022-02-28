import json
import jsonpickle
from collections import Counter
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs


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


class FullResultObject:
    """"Class defines of object to return results in json format
        base_result = AllAlgorithmsResult contains objects of SingleAlgorithmsResult and ComparationResult

        """

    def __init__(self, results_base, full_result, apply_full):
        self.results_base_positive_negative = get_final_answer(results_base)

        self.results_base_information_text_knn = str(dict(Counter(results_base.knn_results.best_params)))
        self.results_base_information_text_svm = str(dict(Counter(results_base.svm_results.best_params)))
        self.results_base_information_text_rf = str(dict(Counter(results_base.svm_results.best_params)))
        self.results_base_accuracy_text_knn = str(results_base.knn_results.score * 100) + "%"
        self.results_base_accuracy_text_svm = str(results_base.svm_results.score * 100) + "%"
        self.results_base_accuracy_text_rf = str(results_base.rf_results.score * 100) + "%"

        self.results_base_knn_plot = results_base.knn_results.plot1
        self.accuracy_imputed_mean_knn = str(results_base.knn_results.result[0])
        self.accuracy_imputed_median_knn = str(results_base.knn_results.result[1])
        self.accuracy_imputed_most_constant_knn = str(results_base.knn_results.result[2])
        self.accuracy_imputed_most_frequent_knn = str(results_base.knn_results.result[3])

        self.results_base_svm_plot = results_base.svm_results.plot1
        self.accuracy_imputed_mean_svm = str(results_base.svm_results.result[0])
        self.accuracy_imputed_median_svm = str(results_base.svm_results.result[1])
        self.accuracy_imputed_most_constant_svm = str(results_base.svm_results.result[2])
        self.accuracy_imputed_most_frequent_svm = str(results_base.svm_results.result[3])

        self.results_base_rf_plot = results_base.rf_results.plot1
        self.accuracy_imputed_mean_rf = str(results_base.rf_results.result[0])
        self.accuracy_imputed_median_rf = str(results_base.rf_results.result[1])
        self.accuracy_imputed_most_constant_rf = str(results_base.rf_results.result[2])
        self.accuracy_imputed_most_frequent_rf = str(results_base.rf_results.result[3])

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

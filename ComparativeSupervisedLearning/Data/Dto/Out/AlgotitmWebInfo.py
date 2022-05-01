import jsonpickle


class AlgorithmWebInfo:
    """"Class defines of object to return results in json
     format for page with information about all algorithms   """

    def __init__(self, info):

        self.time_knn = info[0][0][8]
        self.time_svm = info[1][0][8]
        self.time_rf = info[2][0][8]

        self.best_estimator_plot_1_knn = info[12][0]
        self.best_estimator_plot_2_knn = info[12][1]
        self.best_estimator_plot_1_svm = info[12][2]
        self.best_estimator_plot_2_svm = info[12][3]
        self.best_estimator_plot_1_rf = info[12][4]
        self.best_estimator_plot_2_rf = info[12][5]

        info_to_split_1 = (info[0][0][0]).split("|")
        self.card_text_knn_1 = info_to_split_1[0]
        self.card_text_knn_1_1 = info_to_split_1[1]
        self.card_text_knn_1_2 = info_to_split_1[2]

        info_to_split_2 = (info[1][0][0]).split("|")
        self.card_text_svm_1 = info_to_split_2[0]
        self.card_text_svm_1_1 = info_to_split_2[1]
        self.card_text_svm_1_2 = info_to_split_2[2]

        info_to_split_3 = (info[2][0][0]).split("|")
        self.card_text_rf_1 = info_to_split_3[0]
        self.card_text_rf_1_1 = info_to_split_3[1]
        self.card_text_rf_1_2 = info_to_split_3[2]

        self.accuracy_imputed_mean_knn = str(info[0][0][3])
        self.accuracy_imputed_median_knn = str(info[3][0][3])
        self.accuracy_imputed_most_constant_knn = str(info[6][0][3])
        self.accuracy_imputed_most_frequent_knn = str(info[9][0][3])
        self.accuracy_imputed_mean_svm = str(info[1][0][3])
        self.accuracy_imputed_median_svm = str(info[4][0][3])
        self.accuracy_imputed_most_constant_svm = str(info[7][0][3])
        self.accuracy_imputed_most_frequent_svm = str(info[10][0][3])
        self.accuracy_imputed_mean_rf = str(info[2][0][3])
        self.accuracy_imputed_median_rf = str(info[5][0][3])
        self.accuracy_imputed_most_constant_rf = str(info[8][0][3])
        self.accuracy_imputed_most_frequent_rf = str(info[11][0][3])
        self.results_base_information_text_knn = str(info[13][0])
        self.results_base_information_text_svm = str(info[13][1])
        self.results_base_information_text_rf = str(info[13][2])

    def to_json(self):
        return jsonpickle.encode(self)

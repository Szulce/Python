import jsonpickle


class AlgorithmWebInfo:
    """"Class defines of object to return results in json format      """

    def __init__(self, info):
        self.card_text_knn_1 = info[0][0]
        self.card_text_knn_1_1 = info[0][1]
        self.card_text_knn_1_2 = info[0][2]

        self.card_text_svm_1 = info[1][0]
        self.card_text_svm_1_1 = info[1][1]
        self.card_text_svm_1_2 = info[1][2]

        self.card_text_rf_1 = info[2][0]
        self.card_text_rf_1_1 = info[2][1]
        self.card_text_rf_1_2 = info[2][2]

        self.card_text_knn_svm_text = info[3][0]
        self.card_text_knn_rf_text = info[3][1]
        self.card_text_svm_rf_text = info[3][2]
        self.card_text_svm_rf_plot = info[3][3]
        self.card_text_knn_sv_plot = info[3][4]
        self.card_text_knn_rf_plot = info[3][5]

        self.card_plot_all_1 = info[3][6]
        self.card_plot_all_2 = info[3][7]
        self.card_plot_all_3 = info[3][8]
        self.card_plot_all_4 = info[3][9]
        self.card_plot_all_5 = info[3][10]

    def to_json(self):
        return jsonpickle.encode(self)

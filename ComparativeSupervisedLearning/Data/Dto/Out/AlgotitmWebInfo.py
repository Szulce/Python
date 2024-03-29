import jsonpickle


class AlgorithmWebInfo:
    """"Class defines of object to return results in json
     format for page with information about all algorithms   """

    def __init__(self, information_object):
        """"
        information_object is regular table object containing :
        -description,
        -plots,
        -best params
        for every algorythm for every imputer.

           """

        # KNN mean

        self.knn_mean_desc = information_object[0][0][0]
        self.knn_mean_plot1 = information_object[1][0]
        self.knn_mean_plot2 = information_object[1][1]
        self.knn_mean_best_params = str(information_object[2][0])

        # SVM mean

        self.svm_mean_desc = information_object[3][0][0]
        self.svm_mean_plot1 = information_object[4][0]
        self.svm_mean_plot2 = information_object[4][1]
        self.svm_mean_best_params = str(information_object[5][0])

        # RF mean

        self.rf_mean_desc = information_object[6][0][0]
        self.rf_mean_plot1 = information_object[7][0]
        self.rf_mean_plot2 = information_object[7][1]
        self.rf_mean_best_params = str(information_object[8][0])

        # KNN median

        self.knn_median_desc = information_object[9][0][0]
        self.knn_median_plot1 = information_object[10][0]
        self.knn_median_plot2 = information_object[10][1]
        self.knn_median_best_params = str(information_object[11][0])

        # SVM median

        self.svm_median_desc = information_object[12][0][0]
        self.svm_median_plot1 = information_object[13][0]
        self.svm_median_plot2 = information_object[13][1]
        self.svm_median_best_params = str(information_object[14][0])

        # RF median

        self.rf_median_desc = information_object[15][0][0]
        self.rf_median_plot1 = information_object[16][0]
        self.rf_median_plot2 = information_object[16][1]
        self.rf_median_best_params = str(information_object[17][0])

        # KNN most frequent

        self.knn_freq_desc = information_object[18][0][0]
        self.knn_freq_plot1 = information_object[19][0]
        self.knn_freq_plot2 = information_object[19][1]
        self.knn_freq_best_params = str(information_object[20][0])

        # SVM most frequent

        self.svm_freq_desc = information_object[21][0][0]
        self.svm_freq_plot1 = information_object[22][0]
        self.svm_freq_plot2 = information_object[22][1]
        self.svm_freq_best_params = str(information_object[23][0])

        # RF most frequent

        self.rf_freq_desc = information_object[24][0][0]
        self.rf_freq_plot1 = information_object[25][0]
        self.rf_freq_plot2 = information_object[25][1]
        self.rf_freq_best_params = str(information_object[26][0])

        # KNN -1

        self.knn_cont_desc = information_object[27][0][0]
        self.knn_cont_plot1 = information_object[28][0]
        self.knn_cont_plot2 = information_object[28][1]
        self.knn_cont_best_params = str(information_object[29][0])

        # SVM -1

        self.svm_cont_desc = information_object[30][0][0]
        self.svm_cont_plot1 = information_object[31][0]
        self.svm_cont_plot2 = information_object[31][1]
        self.svm_cont_best_params = str(information_object[32][0])

        # RF -1

        self.rf_cont_desc = information_object[33][0][0]
        self.rf_cont_plot1 = information_object[34][0]
        self.rf_cont_plot2 = information_object[34][1]
        self.rf_cont_best_params = str(information_object[35][0])

        self.time_knn_train = max(information_object[0][0][8], information_object[9][0][8],
                                  information_object[18][0][8],
                                  information_object[27][0][8])
        self.time_svm_train = max(information_object[3][0][8], information_object[12][0][8],
                                  information_object[21][0][8],
                                  information_object[30][0][8])
        self.time_rf_train = max(information_object[6][0][8], information_object[15][0][8],
                                 information_object[24][0][8],
                                 information_object[33][0][8])

        self.time_knn_predict = max(information_object[0][0][9], information_object[9][0][9],
                                    information_object[18][0][9],
                                    information_object[27][0][9])
        self.time_svm_predict = max(information_object[3][0][9], information_object[12][0][9],
                                    information_object[21][0][9],
                                    information_object[30][0][9])
        self.time_rf_predict = max(information_object[6][0][9], information_object[15][0][9],
                                   information_object[24][0][9],
                                   information_object[33][0][9])

        self.classification_report_knn_1 = information_object[0][0][10]
        self.classification_report_knn_2 = information_object[9][0][10]
        self.classification_report_knn_3 = information_object[18][0][10]
        self.classification_report_knn_4 = information_object[27][0][10]

        self.classification_report_svm_1 = information_object[3][0][10]
        self.classification_report_svm_2 = information_object[12][0][10]
        self.classification_report_svm_3 = information_object[21][0][10]
        self.classification_report_svm_4 = information_object[30][0][10]

        self.classification_report_rf_1 = information_object[6][0][10]
        self.classification_report_rf_2 = information_object[15][0][10]
        self.classification_report_rf_3 = information_object[24][0][10]
        self.classification_report_rf_4 = information_object[33][0][10]

        self.confusion = information_object[36]
        self.another_1_knn_param = information_object[37][0]
        self.another_1_knn_time = information_object[37][1]
        self.another_1_svm_param = information_object[37][2]
        self.another_1_svm_time = information_object[37][3]
        self.another_1_rf_param = information_object[37][4]
        self.another_1_rf_time = information_object[37][5]




    def to_json(self):
        return jsonpickle.encode(self)

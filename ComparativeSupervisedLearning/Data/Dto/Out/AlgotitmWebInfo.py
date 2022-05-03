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
          explanation :
          info[0][0] contains description for knn with imputer mean
          info[1][0] contains params plot for knn with imputer mean
          info[1][1] contains second plot for knn with imputer mean
          info[2][0] contains  best estimator params for knn with imputer mean

          info[3][0] contains description for svm with imputer mean
          info[4][0] contains params plot for svm with imputer mean
          info[4][1] contains second plot for svm with imputer mean
          info[5][0] contains  best estimator params for svm with imputer mean

          ...

          info[33][0] contains description for random forest with constant imputer -1
          info[34][0] contains params plot for random forest with  constant imputer -1
          info[34][1] contains second plot for random forest with constant imputer -1
          info[35][0] contains  best estimator params for random forest with  constant imputer -1

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
        self.rf_mean_beast_params = str(information_object[8][0])

        # KNN median

        self.knn_median_desc = information_object[9][0][0]
        self.knn_median_plot1 = information_object[10][0]
        self.knn_median_plot2 = information_object[10][1]
        self.knn_median_beast_params = str(information_object[11][0])

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

        self.time_knn = max(information_object[0][0][9], information_object[9][0][9], information_object[18][0][9], information_object[27][0][9])
        self.time_svm = max(information_object[3][0][9], information_object[12][0][9], information_object[21][0][9], information_object[30][0][9])
        self.time_rf = max(information_object[6][0][9], information_object[15][0][9], information_object[24][0][9], information_object[33][0][9])

        self.confusion = information_object[36]

    def to_json(self):
        return jsonpickle.encode(self)

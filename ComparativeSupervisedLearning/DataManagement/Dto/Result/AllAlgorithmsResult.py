import json


class AllAlgorithmsResult:
    """"Class defines of object to store results of all PredictionManagement"""

    def __init__(self, results_knn, results_svm, results_rf):
        self.percentageKNN = results_knn.percentage
        self.percentageSVM = results_svm.percentage
        self.percentageRF = results_rf.percentage

    def to_string(self):
        print(self)

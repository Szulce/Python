import json


class AllAlgorithmsResult:
    """"Class defines of object to store results of all PredictionManagement"""

    def __init__(self, result_object):
        # todo percentage na true false
        print(result_object)
        if len(result_object) != 0:
            self.percentageKNN = 0.2
            self.percentageSVM = 0.3
            self.percentageRF = 0.4
            self.scoreKNN = 0.5
            self.scoreSVM = 0.6
            self.scoreRF = 0.7

    def to_string(self):
        print(self)

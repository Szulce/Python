import json


class AllAlgorithmsResult:
    """"Class defines of object to store results of all PredictionManagement"""

    def __init__(self, results, scores):
        # todo percentage na true false
        print(results)
        if len(results) != 0:
            self.percentageKNN = results[0][0][0][0]
            self.percentageSVM = results[1][0][0][0]
            self.percentageRF = results[2][0][0][0]
            self.scoreKNN = scores[0][0]
            self.scoreSVM = scores[1][0]
            self.scoreRF = scores[2][0]

    def to_string(self):
        print(self)

import json


class SingleAlgorithmResult:
    """"Class defines of object to store results returned by single algorithm"""

    def __init__(self, plot1, accuracy_score, prediction_model, result):
        self.plot1 = plot1
        self.score = prediction_model.best_score_
        self.result = result
        self.best_params = prediction_model.best_params_
        self.accuracy_score = accuracy_score

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

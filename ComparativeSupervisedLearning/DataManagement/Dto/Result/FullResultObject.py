import json


class FullResultObject:
    """"Class defines of object to store results returned as JSON"""

    def __init__(self, results_base, results_full, apply_extended):
        self.results_base = results_base
        self.results_base_information_text = " Wynik : \nKNN : " + str(results_base.percentageKNN) + " \nSVM : " + str(
            results_base.percentageKNN) + " \nRF : " + str(results_base.percentageRF)
        self.results_base_accuracy_text = "Dokładność: \nKNN : " + str(results_base.scoreKNN) + " \nSVM : " + str(
            results_base.scoreKNN) + " \nRF : " + str(results_base.scoreRF)
        self.results_full = results_full
        self.apply_extended = apply_extended

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

import json


class AllAlgorithmsResult:
    """"Class defines of object to store results of all Management"""

    def __init__(self, result_object, comparison_object):
        # todo percentage na true false
        print(result_object)
        if len(result_object) != 0:
            self.knn_results = result_object[0]
            self.svm_results = result_object[1]
            self.rf_results = result_object[2]
            self.comparison_results = comparison_object

    def to_string(self):
        print(self)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

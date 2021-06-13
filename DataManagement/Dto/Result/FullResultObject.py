import json


class FullResultObject:
    """"Class defines of object to store results returned as JSON"""

    def __init__(self, results_base, results_full):
        self.results_base = results_base
        self.results_full = results_full

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

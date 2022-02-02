class SingleAlgorithmResult:
    """"Class defines of object to store results returned from single algorithm"""

    def __init__(self, percentage):
        self.percentage = percentage

    def to_string(self):
        print(self)

class SingleAlgorithmResult:
    """"Class defines of object to store results returned from single algorithm"""

    def __init__(self, result):
        print("result before conversion to send")
        print(result)
        self.result = result
        self.percentage = 45/100

    def to_string(self):
        print(self)

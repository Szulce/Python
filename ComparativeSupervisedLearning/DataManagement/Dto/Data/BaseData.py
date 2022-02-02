class BaseData:
    """"Class defines of object to store basic features used in process of learning"""

    def __init__(self, form):
        self.age = form.get('age')
        self.sex = form.get('sex')
        self.cp = form.get('cp')
        self.trestbps = form.get('trestbps')
        self.chol = form.get('chol')
        self.fbs = form.get('fbs')
        self.restecg = form.get('restecg')
        self.thalach = form.get('thalach')
        self.exang = form.get('exang')
        self.oldpeak = form.get('oldpeak')
        self.slope = form.get('slope')
        self.ca = form.get('ca')
        self.thal = form.get('thal')

    def to_string(self):
        """"Prints all class attributes values"""
        print(self)
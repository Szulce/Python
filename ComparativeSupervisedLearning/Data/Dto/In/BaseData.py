import pandas
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs
import pandas

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs


class BaseData:
    """"Class defines of object to store basic features used in process of learning"""

    def __init__(self, form):
        if form.get('age') != '':
            self.age = form.get('age')
        else:
            self.age = -1
        self.sex = form.get('sex')
        self.cp = form.get('cp')
        if form.get('trestbps') != '':
            self.trestbps = form.get('trestbps')
        else:
            self.trestbps = -1
        if form.get('chol') != '':
            self.chol = form.get('chol')
        else:
            self.chol = -1
        if form.get('fbs') is not None:
            self.fbs = form.get('fbs')
        else:
            self.fbs = -1
        if form.get('restecg') is not None:
            self.restecg = form.get('restecg')
        else:
            self.restecg = -1
        if form.get('thalach') != '':
            self.thalach = form.get('thalach')
        else:
            self.thalach = -1
        if form.get('exang') is not None:
            self.exang = form.get('exang')
        else:
            self.exang = -1
        if form.get('oldpeak') is not None:
            self.oldpeak = form.get('oldpeak')
        else:
            self.oldpeak = -1
        if form.get('slope') is not None:
            self.slope = form.get('slope')
        else:
            self.slope = -1
        self.ca = form.get('ca')
        categorical_value_thal = form.get('thal')
        if categorical_value_thal == 'N':
            self.thal = 1
        elif categorical_value_thal == 'FD':
            self.thal = 3
        elif categorical_value_thal == 'RD':
            self.thal = 4
        else:
            self.thal = form.get('thal')

    def to_string(self):
        """"Prints all class attributes values"""
        print(self)

    def to_data_frame(self):
        """" Converts to dataFrame """
        list_enumerated = {'age': [self.age], 'sex': [self.sex], 'cp': [self.cp], 'trestbps': [self.trestbps],
                           'chol': [self.chol], 'fbs': [self.fbs], 'restecg': [self.restecg], 'thalach': [self.thalach],
                           'exang': [self.exang], 'oldpeak': [self.oldpeak],
                           'slope': [self.slope], 'ca': [self.ca], 'thal': [self.thal]}
        corrected_df = pandas.DataFrame(list_enumerated, columns=Rs.features_prediction)
        return corrected_df



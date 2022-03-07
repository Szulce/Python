import pandas
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs

class FullData:
    """"Class defines of object to store all possible features used in process of learning"""

    def __init__(self, form):
        self.applyFullResult = form.get('applyExtended')
        self.age = form.get('age')
        self.sex = form.get('sex')
        self.painloc = form.get('painloc')
        self.painexer = form.get('painexer')
        self.relrest = form.get('relrest')
        self.pncaden = form.get('pncaden')
        self.cp = form.get('cp')
        self.trestbps = form.get('trestbps')
        self.htn = form.get('htn')
        self.chol = form.get('chol')
        self.smoke = form.get('smoke')
        self.cigs = form.get('cigs')
        self.years = form.get('years')
        self.fbs = form.get('fbs')
        self.dm = form.get('dm')
        self.famhist = form.get('famhist')
        self.restecg = form.get('restecg')
        self.ekgmo = form.get('ekgmo')
        self.ekgday = form.get('ehgday')
        self.ekgyr = form.get('ekgyr')
        self.dig = form.get('dig')
        self.prop = form.get('prop')
        self.nitr = form.get('nitr')
        self.pro = form.get('pro')
        self.diuretic = form.get('diurentic')
        self.proto = form.get('proto')
        self.thaldur = form.get('thaldur')
        self.thaltime = form.get('thaltime')
        self.met = form.get('met')
        self.thalach = form.get('thalach')
        self.thalrest = form.get('thalrest')
        self.tpeakbps = form.get('tpeakbps')
        self.tpeakbpd = form.get('tpeakbpd')
        self.trestbpd = form.get('trestbpd')
        self.exang = form.get('exang')
        self.xhypo = form.get('xhypo')
        self.oldpeak = form.get('oldpeak')
        self.slope = form.get('slope')
        self.rldv5 = form.get('rldv5')
        self.rldv5e = form.get('rldv5e')
        self.ca = form.get('ca')
        self.restef = form.get('restef')
        self.restwm = form.get('restwm')
        self.exeref = form.get('exeref')
        self.exerwm = form.get('exerwm')
        self.thal = form.get('thal')

    def to_string(self):
        """"Prints all class attributes values"""
        print(self)

    def to_data_frame(self):
        """" Converts to dataFrame """
        return pandas.DataFrame(self, columns=Rs.features_all)

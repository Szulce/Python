import json
import jsonpickle
from collections import Counter
import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs


class DataResultObject:
    """"Class defines of object to return results in json format      """

    def __init__(self, plots, exhibit, gender, distribution, coleration):
        self.exhibit_heart_disease = exhibit[0]
        self.exhibit_heart_disease_gender = exhibit[1]
        self.gender_heart_disease = gender
        self.age_healt_state = plots[1]
        self.distribution_heart_disease = distribution
        self.coleration_heart_disease = coleration
        self.gender_healt_state = plots[0]
        self.healt_state_plot1 = plots[2]
        self.healt_state_plot2 = plots[3]
        self.healt_state_plot3 = plots[4]
        self.healt_state_plot4 = plots[5]
        self.healt_state_plot5 = plots[6]
        self.healt_state_plot6 = plots[7]
        self.healt_state_plot7 = plots[8]
        self.healt_state_plot8 = plots[9]
        self.healt_state_plot9 = plots[10]
        self.healt_state_plot10 = plots[11]
        self.healt_state_plot11 = plots[12]

    def to_json(self):
        return jsonpickle.encode(self)

    # def __reduce__(self):
    #     return (DataResultObject, (self.exhibit_heart_disease ,
    #     self.exhibit_heart_disease_gender,
    #     self.gender_heart_disease,
    #     self.age_healt_state,
    #     self.distribution_heart_disease ,
    #     self.coleration_heart_disease,
    #     self.gender_healt_state ,
    #     self.healt_state_plot1 ,
    #     self.healt_state_plot2 ,
    #     self.healt_state_plot3 ,
    #     self.healt_state_plot4 ,
    #     self.healt_state_plot5 ,
    #     self.healt_state_plot6 ,
    #     self.healt_state_plot7 ,
    #     self.healt_state_plot8 ,
    #     self.healt_state_plot9 ,
    #     self.healt_state_plot10 ))

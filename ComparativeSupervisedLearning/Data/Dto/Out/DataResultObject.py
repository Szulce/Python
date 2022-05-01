import jsonpickle


class DataResultObject:
    """"Class defines of object to return results in json format for data information page   """

    def __init__(self, plots, exhibit, gender, distribution, coleration):
        self.exhibit_heart_disease = exhibit[0]
        self.exhibit_heart_disease_gender = exhibit[1]
        self.gender_heart_disease = gender
        self.age_health_state = plots[1]
        self.distribution_heart_disease = distribution
        self.coleration_heart_disease = coleration
        self.gender_health_state = plots[0]
        self.health_state_plot1 = plots[2]
        self.health_state_plot2 = plots[3]
        self.health_state_plot3 = plots[4]
        self.health_state_plot4 = plots[5]
        self.health_state_plot5 = plots[6]
        self.health_state_plot6 = plots[7]
        self.health_state_plot7 = plots[8]
        self.health_state_plot8 = plots[9]
        self.health_state_plot9 = plots[10]
        self.health_state_plot10 = plots[11]
        # data plot of features divided ill/not ill
        self.health_state_plot11 = plots[12]

    def to_json(self):
        return jsonpickle.encode(self)

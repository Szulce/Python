from ComparativeSupervisedLearning.PredictionManagement import PredictionManager
from ComparativeSupervisedLearning.PredictionManagement import AutoModel as Au
from ComparativeSupervisedLearning.DataManagement.Dto.Result.FullResultObject import FullResultObject

PREDICTION_ESTABLISHED = True


def main():
    # warnings.filterwarnings("ignore", "Mean of empty slice")
    # if PREDICTION_ESTABLISHED:
    # start
    # wczytanie danych(tstowych wyników z wcześniej)
    # dc.readPrediction('ALL')
    # uczenie atosklearn
    # au.run_1()
    Au.run_2()
    # uczenie lasy
    # -> konfiguracje (uzupełnianie danych - > średnia zera ,
    #               usuównaie woerszy,mode -> różne feature brane zza ważniejsze, ilość wywołań ,hiperparametry )
    # df.run()
    # testowanie
    # uczenie knn
    # kn.run()
    # uczenie svm
    # sv.run()
    # wizualizacja wyników

    # porównianie danych
    # algorytmy miedzy sobą
    # algorytmy a auto

    # modul z wystawionym api
    # else:
    #     # tylko predykcja na pdstawie nowych danych
    #     print("todo")


def predict_based_on_user_input(base_data, full_data):
    base_result = PredictionManager.predict_base_data(base_data)
    full_result = PredictionManager.predict_full_data(full_data)
    return FullResultObject(base_result, full_result, full_data.applyFullResult).to_json()


if __name__ == '__main__':
    PredictionManager.train_algorithms()

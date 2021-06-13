import PredictionManagment
from PredictionManagment import AutoModel as Au
import DataManagement.Dto.Result.FullResultObject as FullResult
import DataManagement.DataConversion

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


def predictBasedOnUserInput(base_data, full_data):
    base_result = PredictionManagment.predictBaseData(base_data)
    full_result = PredictionManagment.predictFullData(full_data)
    return FullResult.FullResultObject(base_result, full_result).toJson()


if __name__ == '__main__':
    main()

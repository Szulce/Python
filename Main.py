from Algorithms import AutoModel as au
import pickle
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
    au.run_2()
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
    model = DataManagement.DataConversion.getModel()
    base_result = "4"  # model.predict(base_data)
    full_result = "5"  # model.predict(full_data)
    return tuple([base_result, full_result])


if __name__ == '__main__':
    main()

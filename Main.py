import logging as log
from DataManagement import DataConversion as dc
from Algorithms import AutoModel as au
from Algorithms import DecisionsForest as df
from Algorithms import Knn as kn
from Algorithms import Svm as sv
from Presentation import *
from Results import *
import warnings

PREDICTION_ESTABLISHED = True


def main():
    # warnings.filterwarnings("ignore", "Mean of empty slice")
    if PREDICTION_ESTABLISHED:
        # start
        # wczytanie danych(tstowych wyników z wcześniej)
        # dc.readPrediction('ALL')
        # uczenie atosklearn
        au.run_1()
        # au.run_2()
        # uczenie lasy
        # -> konfiguracje (uzupełnianie danych - > średnia zera ,
        #               usuównaie woerszy,mode -> różne feature brane zza ważniejsze, ilość wywołań ,hiperparametry )
        df.run()
        # testowanie
        # uczenie knn
        kn.run()
        # uczenie svm
        sv.run()
        # wizualizacja wyników

        # porównianie danych
        # algorytmy miedzy sobą
        # algorytmy a auto

        # modul z wystawionym api
    else:
        # tylko predykcja na pdstawie nowych danych
        print("todo")


if __name__ == '__main__':
    main()
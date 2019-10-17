import pandas as ps
# TODO get from user info start algorythm, display perform oraz comparation
from pip._vendor.distlib.compat import raw_input

filePath = raw_input("dataset path? ")

fileDataSet = ps.read_fwf(filePath, ',')

fileDataSet.head()

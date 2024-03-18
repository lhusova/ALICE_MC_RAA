import numpy as np

def create_dictionary(li):
    dictionary = {}
    for i in li:
        if (type(i[0]) != int or type(i[1]) != int ):
            raise ValueError("Die Liste darf nur ganze Zahlen beinhalten!")
        dictionary[str(i[0]) + "-" + str(i[1])] = i
    for i in dictionary:
        print("processing centrality range: " + str(i) + "% - (" + str(dictionary[i][0]) + "/" + str(dictionary[i][1]) + ")")
    return dictionary

def create_event_histos(input):
    return np.histogram(input, bins=200, range=(0,2000))

def count_lines(file):
    with open(file, 'r') as f:
        nLines=0
        for line in f:
            nLines += 1
    return nLines

def find_centralities(dic, value):
    ret = []
    for key in dic:
        if (dic[key][0] <= value and dic[key][1] > value):
            ret.append(key)
    return ret

def get_bin_width(bins):
    fBinWidth=[]
    nBins = len(bins)-1
    for i in range(0,nBins):
        fBinWidth.append((bins[i+1]-bins[i]))
    return fBinWidth

def get_bins():
    fBinsPt = [0.175, 0.225, 0.275, 0.325, 0.375, 0.425, 0.475, 0.525,
               0.575, 0.625, 0.675, 0.725, 0.775, 0.825, 0.875, 0.925, 0.975, 1.05, 1.15,
               1.25, 1.35, 1.45, 1.55, 1.65, 1.75, 1.85, 1.95, 2.1, 2.3, 2.5,
               2.7,2.9, 3.1, 3.3, 3.5, 3.7, 3.8, 4.25, 4.75, 5.25,
               5.75, 6.25,  6.75, 7.5, 8.5,9.5, 10.5,11.5, 12.5, 13.5, 14.5]
    return fBinsPt

def uncertaintyCalculation(h1, h1err, nc1, h2, h2err, nc2):
    return np.sqrt((np.divide(h1err*nc2,h2*nc1))**2 + (np.divide(h1*nc2*h2err,h2*h2*nc1))**2)

#def fill_hist(hist, bins, value):
#    return hist + np.histogram(value, bins)[0]

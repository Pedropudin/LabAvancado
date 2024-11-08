from scipy import constants
import math as mt
import numpy as np

def convertComp_Freq(med):
    return constants.c/med

def convertIndice_freq(i,nTotal,freqSample):
    return i*freqSample/nTotal

def meanSample(sample,inicio,fim):
    soma = 0
    for i in range(inicio,fim):
        soma += sample[i]

    return soma/(fim-inicio)

def makeFunction(amplitude, frequencia,index):
    return amplitude*np.exp(2j * np.pi * frequencia * index)
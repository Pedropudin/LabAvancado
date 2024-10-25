import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from scipy import stats
from scipy import constants
from uncertainties import ufloat

dataPath = "Dados/constante-"
dataPathEnd = ".csv"
resultPath = "Resultados/"

tempList = [-0.5,8.6,24.5,38.7,80.0]
tempPath = ["-0_5","8_6","24_5","38_7","80_0"]

tempUncert = 0.5

ratioList = []

fazerTodos = False

ratioExact = constants.e/constants.k

file = open(resultPath + "results.txt", "w")

file.write(f"Valor Tabelado: {ratioExact}\n")

for i in range(len(tempList)):
    data = pd.read_csv(dataPath + tempPath[i] + dataPathEnd)

    temp = tempList[i]

    tensao = data["tensao"].to_numpy()
    corrente = data["corrente(mA)"].to_numpy()*1e-3

    tensao = tensao[3:-1]
    corrente = corrente[3:-1]
    log_corrente = np.log(corrente)

    reg = stats.linregress(tensao,log_corrente)

    if(fazerTodos == False):
        plt.yscale("log")

    slope = reg[0]
    intercept = reg[1]

    plt.plot(tensao,corrente*1e3,"o",label = f"T={tempList[i]}")
    plt.xlabel("Tensão (V)")
    plt.ylabel("Corrente (mA)")

    plt.grid(True)
    if(fazerTodos == False):
        plt.savefig(resultPath + f"constante-{tempPath[i]}.png")
        plt.clf()

    t = ufloat(temp+273,tempUncert)
    s = ufloat(slope,reg[4])

    ratioMeasured = s*t

    ratioList.append(ratioMeasured)

    if(ratioMeasured.nominal_value - 3*ratioMeasured.std_dev <= ratioExact):
        c = "Sim"
    else:
        c = "Não"

    file.write(f"Temperatura: {temp}\t")
    file.write(f"Razão: {ratioMeasured.nominal_value:.3f} +/- {ratioMeasured.std_dev:.3f} \t")
    file.write(f"Erro Relativo: {(abs(ratioMeasured.nominal_value-ratioExact)/ratioExact) * 100:.3f}%\t")
    file.write(f"Condizente: {c}")
    file.write("\n")

m = sum(ratioList)
m = m/len(ratioList)

file.write(f"Media: {m}")

if(fazerTodos):
    plt.legend()
    plt.savefig(resultPath + f"constante-todos.png")
    plt.clf()

file.close()
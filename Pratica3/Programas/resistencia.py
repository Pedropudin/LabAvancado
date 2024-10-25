import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from scipy import stats
from scipy import constants

dataPath = "Dados/resistencia-"
dataPathEnd = ".csv"
resultPath = "Resultados/"

tempList = [-5.6, 5.4, 32.5, 54.2, 91.0]
tempPath = ["-5_6", "5_4", "32_5", "54_2", "91_0"]

rList = []

file = open(resultPath + "resistencia.txt", "w")

for i in range(len(tempList)):

    data = pd.read_csv(dataPath + tempPath[i] + dataPathEnd)

    temp = tempList[i]

    tensao = data["tensao"].to_numpy()
    corrente = data["corrente(mA)"].to_numpy()*1e-3

    reg = stats.linregress(corrente,tensao)

    rMeasured = reg[0]
    intercept = reg[1]

    plt.plot(corrente,tensao,"o")
    plt.xlabel("Corrente (A)")
    plt.ylabel("Tensão (V)")

    plt.grid(True)
    plt.savefig(resultPath + f"resistencia-{tempPath[i]}.png")
    plt.clf()

    rList.append(rMeasured)

    file.write(f"Temperatura: {temp}\t")
    file.write(f"Razão: {rMeasured} +/- {reg[4]}")
    file.write("\n")

file.close()

plt.plot(tempList,rList,"o")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistência ($\Omega$)")
plt.grid(True)
plt.savefig(f"{resultPath}resistencia-todas.png")
plt.clf()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functions import *

vermelho = pd.read_csv("Dados/vermelho.csv")
verde = pd.read_csv("Dados/verde.csv")
laranja = pd.read_csv("Dados/laranja.csv")

compVermelho = 632.8e-9
compAmarelo = 594.1e-9
compVerde = 543e-9
freqVermelho = convertComp_Freq(compVermelho)
freqAmarelo = convertComp_Freq(compAmarelo)
freqVerde = convertComp_Freq(compVerde)

R = freqVermelho/(420/2048)


x,y = [],[]
for i in range(0,2048): # Choose number of points to plot
    x.append(vermelho["Indice"][i]*0.2)
    y.append(vermelho["Voltagem"][i] + verde["Voltagem"][i] + laranja["Voltagem"][i])

plt.plot(x,y)
# plt.show()
plt.clf()

transformationComplex = np.fft.fft(y)
transformationAbsolute = np.absolute(transformationComplex)
transformationAbsolute[0] = 0

# Plot fft
x,y = [],[]
for i in range(350,550): # Choose number of points to plot
    x.append(convertComp_Freq(convertIndice_freq(vermelho["Indice"][i],2048,R))*1e9)
    # x.append(vermelho["Indice"][i])
    if(transformationAbsolute[i]<0): # Choose the filter
        y.append(0)
    else:
        y.append(transformationAbsolute[i])

plt.plot(x,y, label = "Medido")
plt.plot([compVermelho*1e9]*2,[0,600], label = "Esperado: Vermelho",linewidth = "2", color="red")
plt.plot([compAmarelo*1e9]*2,[0,600], label = "Esperado: Laranja",linewidth = "2", color="orange")
plt.plot([compVerde*1e9]*2,[0,600], label = "Esperado: Verde",linewidth = "2", color = "green")
plt.legend()
plt.xlabel("Comprimento de Onda ($nm$)")
plt.ylabel("Amplitude")
plt.savefig("Resultados/soma-fft.png", bbox_inches='tight')
plt.show()
plt.clf()
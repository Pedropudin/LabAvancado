# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from functions import *

# Define Variables
resultPath = "Resultados/"
originPath = "Dados/"
filename = "verde+laranja+vermelho"

compVermelho = 632.8e-9
compAmarelo = 594.1e-9
compVerde = 543e-9
freqVermelho = convertComp_Freq(compVermelho)
freqAmarelo = convertComp_Freq(compAmarelo)
freqVerde = convertComp_Freq(compVerde)

R = freqVermelho/(420/2048)

# Get data
data = pd.read_csv(f"{originPath}{filename}.csv") # choose data to use
tamanhoTotal = len(data["Indice"])

# ================ Plot =================== #
x,y = [],[]
xEsp, yEsp = [],[]
for i in range(0,500): # Choose number of points to plot
    x.append(data["Indice"][i]*0.2)
    y.append(data["Voltagem"][i])
    # Tá plotando o esperado num range menor porque multiplica o índice por 0.2
    # for j in range(5):
    #     xEsp.append(data["Indice"][i]+j*0.2)
    #     yEsp.append(makeFunction(0.75,1/5,xEsp[-1]) + 1)

plt.plot(x,y, label = "Medida")
# plt.plot(x,y, "o", color="blue")
# plt.plot(xEsp, yEsp, label = "Esperado")
# plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Voltagem (V)")
# plt.savefig(f"{resultPath}{filename}.png", bbox_inches='tight') # choose filename
plt.show()
plt.clf()

# ================ FFT ================ #
transformationComplex = np.fft.fft(data["Voltagem"])
transformationAbsolute = np.absolute(transformationComplex)
transformationAbsolute[0] = 0

# Plot fft
x,y = [],[]
for i in range(350,500): # Choose number of points to plot
    index = data["Indice"][i]
    x.append(convertComp_Freq(convertIndice_freq(data["Indice"][i],tamanhoTotal,R))*1e9)
    # x.append(data["Indice"][i])
    if(transformationAbsolute[i]<0): # Choose the filter
        y.append(0)
    else:
        y.append(transformationAbsolute[i])

plt.plot(x,y, label="Medido")
plt.plot([compVermelho*1e9]*2,[0,300], label = "Esperado: Vermelho",linewidth = "2", color="red")
# plt.plot([compAmarelo*1e9]*2,[0,1050], label = "Esperado: Laranja",linewidth = "2", color="orange")
# plt.plot([compVerde*1e9]*2,[0,800], label = "Esperado: Verde",linewidth = "2", color = "green")
plt.legend()
plt.xlabel("Comprimento de Onda ($nm$)")
plt.ylabel("Voltagem (V)")
# plt.savefig(f"{resultPath}{filename}-fft.png", bbox_inches='tight') # choose filename
# plt.show()
plt.clf()

# ===================== Extras ===================== #

print(f"{freqVerde:.3e}")

def writeData(data,filename):
    with open(filename,"w") as f:
        for i in range(len(data)):
            f.write(f"{i},{data[i]}\n")
    
    return

writeData(transformationAbsolute, f"{originPath}{filename}-fft.csv")
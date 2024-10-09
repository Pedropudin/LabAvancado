import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from scipy import stats
from scipy import constants

data = pd.read_csv("constante-80_0.csv")

temp = 80

tensao = data["tensao"].to_numpy()
corrente = data["corrente(mA)"].to_numpy()*1e-3

tensao = tensao[3:-1]
corrente = corrente[3:-1]
log_corrente = np.log(corrente)

reg = stats.linregress(tensao,log_corrente)

plt.yscale("log")

slope = reg[0]
intercept = reg[1]

plt.plot(tensao,corrente,"o")
plt.plot(tensao, slope*tensao + intercept)

# print(slope*tensao + intercept)
print(constants.e/constants.k)
print(slope*(temp + 273))

print((slope*(temp + 273))/(constants.e/constants.k))

plt.grid(True)
plt.show()
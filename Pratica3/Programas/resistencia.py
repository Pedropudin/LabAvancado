import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from scipy import stats
from scipy import constants

data = pd.read_csv("Dados/resistencia--5_6.csv")

tensao = data["tensao"].to_numpy()
corrente = data["corrente(mA)"].to_numpy()*1e-3

plt.plot(corrente,tensao,"o")

reg = stats.linregress(corrente,tensao)

print(reg[0])

plt.show()
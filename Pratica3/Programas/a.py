import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from scipy import stats
from scipy import constants

data = pd.read_csv("r.csv")

temperatura = data["temperatura"].to_numpy()
resistencia = data["resistencia"].to_numpy()

plt.plot(temperatura,resistencia,"o")

reg = stats.linregress(temperatura,resistencia)

print(reg[0])

plt.show()
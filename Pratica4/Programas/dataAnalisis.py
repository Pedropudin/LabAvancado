import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

v_l = "Dados/vermelho+laranja.csv"
v = "Dados/vermelho.csv"

data = pd.read_csv(v_l)["Voltagem"]
i = pd.read_csv(v_l)["Indice"]

r = np.fft.fft(data)

print(len(i),len(data))

plt.plot(i[:-500],np.absolute(r)[:-500])
plt.show()

plt.plot(i[:-1000],data[:-1000])
plt.show()
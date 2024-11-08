import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import *
from scipy import stats
data = pd.read_csv("Dados/ressonancia+sonda_hall.csv")

x = data["campo Magnético (mT)"]*1e-3
y = data["frequencia (MHz)"]*1e6
B = np.array([campoHell(6.8e-2,320,x) for x in data["corrente (A)"]])
x = (B/2)
reg = stats.linregress(x,y)
mub = constants.hbar*constants.e/(2*constants.m_e)
g = reg[0]*constants.h/mub

plt.plot(x,y)

plt.show() 

#print(B/2)
print('g: ',g)
print(reg[0]*constants.h/mub,reg[4]*constants.h/mub)
print(campoHell(6.8e-2,320,1))
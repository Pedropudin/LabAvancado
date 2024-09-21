from data import *

freq = [amarelo.getFrequencia(), verde.getFrequencia()]

V0 = [amarelo.getPotencialParada(), verde.getPotencialParada()]

#plt.plot(freq,V0,"o")
#plt.show()

df = int(freq[1]) - int(freq[0])
dV = int(V0[1]) - int(V0[0])

print(df)
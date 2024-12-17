# coding: utf-8
from math import sqrt
dU = 9.5
Umod = 10*5
Imod = 0.273/2*2*sqrt(2)
dI = dU/Umod*Imod
dB = 4.23*dI

dU = 9.5
dU = 8 # resfriado
dU/Umod
dI = dU/Umod*Imod
dB = 4.23*dI
print(dB)
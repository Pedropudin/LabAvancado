from plot import *
from calibracao import *

def convertR_em_T(R,R0,T0):
    return T0 + ((R/R0 - 1)/0.00385)

def getResistencia_G_intrinseco():
    Rt,T,tensao,corrente = getData_array("condutividade-germaio-intrinseco.csv")
    corrente = corrente*1e-3

    return corrente/tensao * 100,T

R,T = getResistencia_G_intrinseco()

g = createGraph()

plotList_line(g,T,R)

axisNames(g,"Temperatura","Condutividade")

showGraph()
from plot import *
from calibracao import *

def graphHall_Germanico():
    Xn,Yn = getData_array('concentracao-Ge-n.csv')
    Xp,Yp = getData_array('concentracao-Ge-p.csv')

    g = createGraph()

    c_linear, convert = coeficientCalibracao()

    plotList_points_regression(g,Xn*convert,Yn)
    plotList_points_regression(g,Xp*convert,Yp)


    axisNames(g,"Campo Magnético (T)","Tensão Hall (V)")

    graphGrid(g)
    showGraph()

    return

def getInfo_Germanico_p():
    """Retorna corrente na placa e tensão na placa"""

    return 0.0303,0.766

def getInfo_Germanico_n():
    """Retorna corrente na placa e tensão na placa"""

    return 0.03,1.134

def getInfo_Cobre():
    """Retorna corrente na placa"""

    return 15.07

def getInfo_Zinco():
    """Retorna corrente na placa"""

    return 14.92

def numeroPortadores(I,B,Vh,l):
    e = -constants.e

    return (I*B)/(Vh*e*l)

#Tensão na placa 1.134 V
#Corrente na placa 30.0 mA
#Corrente na bobina por Tensão Hall
from plot import *

Xn,Yn = getData_list('concentracao-Ge-n.csv')

angularN, linearN, desvioN = linearRegression(Xn,Yn)

def Ge_n(x):
    return angularN * x + linearN

x, yLine_n = listFromFunction(Ge_n, 0,5,0.2)

graph = createGraph()

plotList_points(graph,Xn,Yn,"Germânio-N","red")
plotList_line(graph,np.arange(0,5,0.2),yLine_n,"Fit-N","red")

axisNames(graph,"Corrente","Tensão")

showGraph()

#Tensão na placa 1.134 V
#Corrente na placa 30.0 mA
#Corrente na bobina por Tensão Hall